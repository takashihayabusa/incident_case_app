from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "memo", "priority"]


# ★ Django 5 対応：複数ファイル用 Widget
class MultipleFileInput(forms.FileInput):
    allow_multiple_selected = True


class PostFileForm(forms.Form):
    files = forms.FileField(
        label="添付ファイル（複数選択可）",
        required=False,
        widget=MultipleFileInput()
    )
