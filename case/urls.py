from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("edit/<int:pk>/", views.post_edit, name="post_edit"),
    path("delete/<int:pk>/", views.post_delete, name="post_delete"),
]
