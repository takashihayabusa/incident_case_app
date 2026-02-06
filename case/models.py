from django.db import models


class Post(models.Model):
    PRIORITY_CHOICES = (
        (1, "低"),
        (2, "中"),
        (3, "高"),
    )

    title = models.CharField(max_length=200)
    memo = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # システム用
    incident_date = models.DateField("発生日", null=True, blank=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class PostFile(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="files",
        on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="uploads/")

    def __str__(self):
        return f"{self.post.title} - {self.file.name}"
