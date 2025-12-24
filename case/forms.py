from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    duedate = forms.DateField(
        label="記入日",
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Post
        fields = ["title", "memo", "priority", "duedate"]
