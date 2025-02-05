from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm, PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.urls import reverse, reverse_lazy


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
        'title': post.title,
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

def add_post(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'статья успешно добавлена')
            return redirect(reverse('blog:detail_post', kwargs={'pk':post.pk}))
    form = PostAddForm()
    context = {
        'title': 'Добавить статью',
        'form': form
    }
    return render(request, 'blog/add_post.html', context)

def update_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    form = PostAddForm(request.POST or None, 
                       request.FILES or None, 
                       instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            messages.success(request, 'статья успешно обновлена')
            return redirect(reverse('blog:detail_post', kwargs={'pk':post.pk}))
    context = {
        'title': 'Изменить статью',
        'form': form,
        'update': True
    }
    return render(request, 'blog/add_post.html', context)

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    # success_url = reverse_lazy("blog:index")
    template_name = 'blog/delete_post.html'
    login_url = reverse_lazy('user:login')

    def get_success_url(self) -> str:
        messages.success(self.request, 'Пост успешно удален')
        return reverse('blog:index')
    
    