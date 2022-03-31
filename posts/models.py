from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField()
    caption = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
