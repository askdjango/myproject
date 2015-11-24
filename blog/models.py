from django.conf import settings
from django.db import models


class Post(models.Model):
    # id = PositiveIntegerField(), primary_key
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # 'auth.User'
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # 'auth.User'
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
