from django.urls import path

from . import views

urlpatterns = [
  path("", views.get_posts, name="Posts"),
  path("new/", views.create_post, name="Create Post"),
  path("<int:id>", views.post_detail, name="Manage Post"),
]