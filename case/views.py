from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from collections import Counter
import re

# =====================================
# 店舗名抽出用（最終・安定版）
# ・1～15文字＋「店」で終わる文字列を拾う
# ・拾いすぎないが、拾えなくならない
# =====================================
STORE_RE = re.compile(r'.{1,15}?店')

def home_view(request):
    # =====================
    # 事案一覧（ページネーション）
    # =====================
    qs = Post.objects.all().order_by("-id")

    paginator = Paginator(qs, 10)  # 1ページ10件
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # =====================
    # 店舗別ベスト5（全文から集計）
    # =====================
    stores = []

    for post in qs:
        text = f"{post.title} {getattr(post, 'memo', '')}"

        matches = STORE_RE.findall(text)
        for m in matches:
            # 最低限の安全フィルタ（壊れにくい）
            if "店" in m and len(m) <= 8:
                stores.append(m)

    store_best = Counter(stores).most_common(5)

    # デバッグ確認用（問題なければ後で削除OK）
    print("STORE BEST:", store_best)

    return render(
        request,
        "case/home.html",
        {
            "page_obj": page_obj,
            "store_best": store_best,
        }
    )
