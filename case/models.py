from django.db import models


class Post(models.Model):
    """
    事案（案件）本体
    """

    PRIORITY_CHOICES = [
        ("high", "高"),
        ("medium", "中"),
        ("low", "低"),
    ]

    title = models.CharField(
        "タイトル",
        max_length=200
    )

    memo = models.TextField(
        "内容",
        blank=True
    )

    priority = models.CharField(
        "重要度",
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    created_at = models.DateTimeField(
        "作成日時",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title}（{self.get_priority_display()}）"


class PostFile(models.Model):
    """
    事案に紐づく添付ファイル（複数可）
    """

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="files",
        verbose_name="事案"
    )

    file = models.FileField(
        "添付ファイル",
        upload_to="post_files/"
    )

    uploaded_at = models.DateTimeField(
        "アップロード日時",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.post.title} - {self.file.name}"
