from django.urls import path
from .views import home_view, PostListView, PostDetailView, PostCreateView

app_name = "case"

urlpatterns = [
    path("", home_view, name="home"),
    path("list/", PostListView.as_view(), name="post-list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
]
