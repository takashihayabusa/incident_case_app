import re
from collections import Counter
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count
from .models import Post

import re

def extract_store_name(title):
    """
    タイトル内の店舗名（〇〇店 / 本部）を抽出
    """
    if not title:
        return None

    m = re.search(r"[一-龥ぁ-んァ-ンA-Za-z0-9]+店|本部", title)
    if m:
        return m.group(0)
    return None

def home_view(request):
    q = request.GET.get("q", "")

    posts_qs = Post.objects.order_by("-created_at")

    if q:
        posts_qs = posts_qs.filter(
            Q(title__icontains=q) | Q(memo__icontains=q)
        )

    paginator = Paginator(posts_qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # ===== ベスト5 =====
    counter = Counter()
    for p in posts_qs.only("title"):
        store = extract_store_name(p.title)
        if store:
            counter[store] += 1
    best5 = counter.most_common(5)

    return render(request, "case/home.html", {
        "page_obj": page_obj,
        "best5": best5,
    })

# =========================
# 編集
# =========================
# case/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostFile
from .forms import PostForm

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            # ===== ファイル削除 =====
            delete_ids = request.POST.getlist("delete_files")
            if delete_ids:
                PostFile.objects.filter(
                    id__in=delete_ids,
                    post=post
                ).delete()

            # ===== ファイル追加 =====
            for f in request.FILES.getlist("files"):
                PostFile.objects.create(
                    post=post,
                    file=f
                )

            return redirect("case:home")
    else:
        form = PostForm(instance=post)

    return render(request, "case/post_form.html", {
        "form": form,
        "post": post,
    })


# =========================
# 事案削除
# =========================
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("case:home")

    return render(request, "case/delete_confirm.html", {
        "post": post,
    })


# =========================
# ファイル削除
# =========================
def file_delete(request, file_id):
    file_obj = get_object_or_404(PostFile, id=file_id)
    post_id = file_obj.post.id

    # 実ファイル削除
    file_obj.file.delete()

    # DB削除
    file_obj.delete()

    return redirect("case:post_edit", pk=post_id)

from django.shortcuts import render, redirect
from .forms import PostForm


def post_create(request):
    """
    事案 新規作成
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("case:home")
    else:
        form = PostForm()

    return render(request, "case/post_form.html", {
        "form": form,
    })


# case/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("case:home")

    return render(request, "case/delete_confirm.html", {
        "post": post,
    })

