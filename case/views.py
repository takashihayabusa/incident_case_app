from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'case/home.html', {
        'posts': Post.objects.all()
    })
