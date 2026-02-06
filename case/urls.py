from django.urls import path
from . import views

app_name = "case"

urlpatterns = [
    # 一覧（トップ）
    path("", views.home_view, name="home"),

    # 新規作成
    path("create/", views.post_create, name="post_create"),

    # 編集
    path("edit/<int:pk>/", views.post_edit, name="post_edit"),

    # 削除
    path("delete/<int:pk>/", views.post_delete, name="post_delete"),
]
