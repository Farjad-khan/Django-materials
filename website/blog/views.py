from django.shortcuts import render
from .models import Post

# Home 

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def testimonials(request):
    return render(request, 'blog/testimonials.html')


