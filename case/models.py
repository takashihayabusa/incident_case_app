from django.db import models
from django.utils import timezone


class Post(models.Model):
    created_at = models.DateField(
        verbose_name="記入日",
        default=timezone.now
    )
    store_name = models.CharField(
        "店舗名",
        max_length=100
    )
    title = models.CharField(
        "タイトル",
        max_length=200
    )
    memo = models.TextField(
        "内容",
        blank=True
    )
    file = models.FileField(
        upload_to="uploads/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.store_name}｜{self.title}"
