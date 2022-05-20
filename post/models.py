from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
  author_id = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
      return self.title
