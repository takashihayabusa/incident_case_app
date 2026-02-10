from django import forms
from case.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["store_name", "title", "memo", "file"]
