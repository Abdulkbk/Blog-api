from calendar import c
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['id', 'author_id', 'title', 'content', 'created_at', 'updated_at']