from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

def home_view(request):
    total_cases = Post.objects.count()
    posts = Post.objects.all().order_by("-id")
    return render(request, "case/home.html", {
        "total_cases": total_cases,
        "posts": posts[:5],  # 最新5件だけ
    })

class PostListView(ListView):
    model = Post
    template_name = "case/list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-id"]

class PostDetailView(DetailView):
    model = Post
    template_name = "case/detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "memo", "priority", "duedate"]
    template_name = "case/post_form.html"
    success_url = "/list/"
