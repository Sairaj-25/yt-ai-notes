# 📝 YT-AI-Blog: YouTube to AI Blog Generator

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Django Version](https://img.shields.io/badge/django-5.2-green)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-orange)
![AssemblyAI](https://img.shields.io/badge/Speech_to_Text-AssemblyAI-blueviolet)

<<<<<<< HEAD
🎯 It combines:
- YouTube audio extraction via `yt-dlp`
- Speech-to-text transcription with AssemblyAI
- AI blog generation using OpenAI’s advanced models
=======
**YT-AI-Blog** is a powerful Django-powered web application that takes a YouTube video URL, extracts and transcribes the audio, and leverages Google's Gemini AI to generate a professional, highly-structured blog article or study notes based on the video's content.

🎯 **The Workflow:**
1. **Extract:** Downloads high-quality audio from YouTube via `yt-dlp`.
2. **Transcribe:** Converts speech to text accurately using AssemblyAI.
3. **Generate:** Transforms the raw transcript into clean, readable blog content using the Gemini 2.5 Flash model.
>>>>>>> c11d7175c2d5b0c69c29db6af4658a9f9a4dafc6

---

## 🚀 Features

- **Seamless URL Processing:** Simply paste a YouTube link to generate content.
- **Automated Audio Extraction:** Handles audio downloading and formatting entirely in the background.
- **Smart Formatting:** AI generates structured content with headings, bullet points, and actionable summaries.
- **User Authentication:** Secure login and signup system for users to save and manage their generated blogs.
- **RESTful-Style API:** Includes a dedicated JSON API endpoint (`/generate-blog/`) for background processing.
- **Modern UI:** Clean, responsive frontend built with Tailwind CSS.

---

## 🧠 Tech Stack

<<<<<<< HEAD
| Layer | Technology |
|-------|------------|
| Backend | Django |
| YouTube Extraction | yt-dlp |
| Transcription | AssemblyAI |
| AI Content | OpenAI API |
| Python Version | 3.9+ |
| Database | Django ORM (SQLite default) |
=======
| Component | Technology |
| :--- | :--- |
| **Backend Framework** | Django 5.2 |
| **Video/Audio Downloader**| `yt-dlp` & `ffmpeg` |
| **Speech-to-Text API** | AssemblyAI |
| **Generative AI** | Google Gemini (`google-genai` SDK) |
| **Frontend** | HTML5, Tailwind CSS, JavaScript |
| **Database** | SQLite (Default Django ORM) |
>>>>>>> c11d7175c2d5b0c69c29db6af4658a9f9a4dafc6

---

## ⚙️ Prerequisites

<<<<<<< HEAD
### 1. Clone the repository
```bash
git clone https://github.com/Sairaj-25/yt-ai-blog.git
cd yt-ai-blog
=======
Before you begin, ensure you have the following installed on your machine:
- **Python 3.9+**
- **FFmpeg**: Required by `yt-dlp` to extract and process the audio files.
  - *Windows*: Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) and add to your system PATH.
  - *Mac*: `brew install ffmpeg`
  - *Linux*: `sudo apt install ffmpeg`

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/Sairaj-25/yt-ai-blog.git](https://github.com/Sairaj-25/yt-ai-blog.git)
cd yt-ai-blog
```

### 2. Set up a Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies
 
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

- Create a .env file in the root directory (alongside manage.py) and add your secret keys:
  
```Code snippet
GEMINI_API_KEY="your_google_gemini_api_key_here"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
DJANGO_SECRET_KEY="your_secure_django_secret_key_here"
```

### 5. Apply Database Migrations
- Initialize the SQLite database and create the necessary tables for authentication and blog posts:
  
```bash
python manage.py makemigrations
python manage.py migrate

```

### 6. Run the Development Server

```bash
python manage.py runserver

```
- Open your browser and navigate to: http://127.0.0.1:8000/

🧪 Usage Guide

```
Sign Up / Log In: Create an account to access the dashboard.

Paste Link: On the home page, paste any valid YouTube video URL into the input field.

Generate: Click the "Generate" button. A loading animation will appear while the backend extracts the audio, transcribes it, and queries Gemini.

Read & Save: Once completed, the AI-generated blog article will appear on your screen, complete with formatting, summaries, and key takeaways.
```

🗂 Project Structure
```
yt-ai-blog/
├── ai_blog_app/           # Core Django project settings & routing
├── blog_generator/        # Main application (Models, Views, URLs)
├── media/                 # Temporary storage for downloaded audio files
├── templates/             # HTML templates (Tailwind UI)
├── static/                # Static assets (CSS, JS)
├── .env                   # Environment variables (Ignored by Git)
├── requirements.txt       # Python dependencies
└── manage.py              # Django command-line utility
```

🤝 Contributing


- Contributions, issues, and feature requests are welcome!

- Fork the Project
```
Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

```

## Project Link:
```
https://github.com/Sairaj-25/yt-ai-blog
```
>>>>>>> c11d7175c2d5b0c69c29db6af4658a9f9a4dafc6
