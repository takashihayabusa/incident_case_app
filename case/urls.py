from django.urls import path
from .views import home_view, post_create

app_name = "case"

urlpatterns = [
    path("", home_view, name="home"),
    path("create/", post_create, name="post_create"),
]
