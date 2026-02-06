from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    incident_date = forms.DateField(
        label="発生日",
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date"   # ← カレンダー表示
        })
    )

    class Meta:
        model = Post
        fields = ["title", "memo", "incident_date"]
