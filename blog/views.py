from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User


def home(request):
    post = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'post_list': post
    }
    return render(request, 'index.html', context)


def posts(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def authors(request):
    user = User.objects.all()
    context = {
        'authors': user
    }
    return render(request, 'user_detail.html', context)
