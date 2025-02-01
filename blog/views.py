from django.shortcuts import render
from .models import Category, Post
from django.db.models import F


def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'Блог',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def detail_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.watched = F("watched") + 1
    post.save()
    context = {
        'title': post.title[:10],
        'post': post
    }
    return render(request, 'blog/detail.html', context)

def posts_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=category)
    
    context = {
        'title': 'Блог ' + category.title,
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/index.html', context=context)