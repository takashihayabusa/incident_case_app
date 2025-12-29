from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, PostFile
from .forms import PostForm, PostFileForm
from collections import Counter
import re

STORE_RE = re.compile(r'.{1,15}?店')


def home_view(request):
    qs = Post.objects.all().order_by("-id")

    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    stores = []
    for post in qs:
        text = f"{post.title} {post.memo}"
        matches = STORE_RE.findall(text)
        for m in matches:
            if "店" in m and len(m) <= 8:
                stores.append(m)

    store_best = Counter(stores).most_common(5)

    return render(
        request,
        "case/home.html",
        {
            "page_obj": page_obj,
            "store_best": store_best,
        }
    )


def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        file_form = PostFileForm(request.POST, request.FILES)

        if post_form.is_valid() and file_form.is_valid():
            post = post_form.save()

            for f in request.FILES.getlist("files"):
                PostFile.objects.create(
                    post=post,
                    file=f
                )

            return redirect("case:home")
    else:
        post_form = PostForm()
        file_form = PostFileForm()

    return render(
        request,
        "case/post_form.html",
        {
            "post_form": post_form,   # ★ここが超重要
            "file_form": file_form,
        }
    )
