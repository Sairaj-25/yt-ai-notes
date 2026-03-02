# Django shortcuts for rendering templates and redirecting users
from django.shortcuts import render, redirect

# Django authentication utilities (Restored to default Django User model)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# CSRF exemption for API-style POST requests
from django.views.decorators.csrf import csrf_exempt

# Used to send JSON responses instead of HTML
from django.http import JsonResponse
from django.conf import settings

# Standard libraries
import json
import os

# YouTube audio download library
from yt_dlp import YoutubeDL

# AssemblyAI for speech-to-text
import assemblyai as aai

# Google Gemini SDK (Modern)
from google import genai
from google.genai import types


# -----------------------------
# GLOBAL CLIENT CONFIGURATION
# -----------------------------

# Configure Gemini Client using API key from environment variable
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Set AssemblyAI API key from environment variable
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")


# -----------------------------
# HOME PAGE VIEW
# -----------------------------

@login_required
def index(request):
    return render(request, "index.html")


# -----------------------------
# MAIN BLOG GENERATION API
# -----------------------------

@csrf_exempt
def generate_blog(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)
        yt_link = data.get("link")

        if not yt_link:
            return JsonResponse({"error": "YouTube link is required"}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

    # Fetch YouTube video title
    title = yt_title(yt_link)
    if not title:
        return JsonResponse({"error": "Failed to fetch YouTube title"}, status=500)

    # Convert YouTube audio → text transcript
    transcription = get_transcription(yt_link)
    if not transcription:
        return JsonResponse({"error": "Failed to get transcript"}, status=500)

    # Generate blog article from transcript using Gemini
    blog_content = generate_blog_from_transcription(transcription)
    if not blog_content or "An unexpected error occurred" in blog_content:
        return JsonResponse({"error": blog_content}, status=500)

    # Return generated content as JSON
    return JsonResponse({
        "title": title,
        "content": blog_content
    })


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def yt_title(link):
    """Extracts the video title without downloading the video."""
    try:
        with YoutubeDL() as ydl:
            info = ydl.extract_info(link, download=False)
            return info.get("title", "Unknown Title")
    except Exception as e:
        print(f"YouTube title error: {e}")
        return None


def download_audio(link):
    """Downloads YouTube audio and converts it to MP3."""
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(settings.MEDIA_ROOT, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            mp3_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
            return mp3_path
    except Exception as e:
        print(f"Audio download error: {e}")
        return None


def get_transcription(link):
    """Converts YouTube audio into text using AssemblyAI."""
    try:
        audio_file = download_audio(link)
        if not audio_file:
            return None

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_file)

        os.remove(audio_file)
        return transcript.text
    except Exception as e:
        print(f"Transcription error: {e}")
        return None


def generate_blog_from_transcription(transcription):
    """Uses Google Gemini to generate a structured blog article."""
    try:
        prompt = f"""
        You are a professional AI learning assistant.

Convert this YouTube transcript into high-quality, structured revision notes.

Instructions:

• Extract only meaningful insights.
• Remove filler, jokes, repetition, and promotions.
• Organize content into sections with headings.
• Use bullet points.
• Highlight important keywords in bold.
• Convert explanations into:
  - Definitions
  - Step-by-step processes
  - Tables (if comparison discussed)
  - Flowcharts (text format if needed)
• Add examples separately under an “Examples” section.
• Add a “Quick Revision Box” at the end.
• Add “Actionable Steps” if the video is practical.
• Keep output concise but complete.

Output must look clean, like premium AI-generated notes.

You are an expert academic note generator.
Transform the provided content into professional, high-quality smart notes similar to NoteGPT.
Summarize the following content into smart structured notes:

- Use headings and subheadings
- Bullet format only
- Highlight keywords
- Include summary box at end
- Keep concise but comprehensive
- Make it visually clean and revision-friendly


Transcript:
{transcription}
"""
        # Call Gemini API using the new google-genai SDK
        response = gemini_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are an expert blog writer.",
                temperature=0.7,
                max_output_tokens=8192, # Safe maximum limit
            )
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        return f"An unexpected error occurred: {str(e)}"


# -----------------------------
# AUTH FUNCTIONS
# -----------------------------

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'Login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'Login.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('/')