from django.db import models


PRIORITY_CHOICES = [
    ("high", "高"),
    ("medium", "中"),
    ("low", "低"),
]


class Post(models.Model):
    title = models.CharField("タイトル", max_length=100)
    memo = models.TextField("メモ", blank=True)
    priority = models.CharField(
        "重要度",
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium"
    )
    duedate = models.DateField("記入日")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return f"Case {self.id}"


class PostFile(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="files"
    )
    file = models.FileField(
        "データ",
        upload_to="uploads/",
        blank=True,
        null=True
    )
    uploaded_at = models.DateTimeField("アップロード日時", auto_now_add=True)

    def __str__(self):
        return self.post.title
