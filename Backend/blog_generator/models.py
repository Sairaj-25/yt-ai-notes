from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    # Links the blog post to the user who generated it
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

    # Stores the original YouTube link
    youtube_link = models.URLField(max_length=500)

    # Stores the generated title and content
    title = models.CharField(max_length=300)
    content = models.TextField()

    # Automatically records when the blog was generated
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
