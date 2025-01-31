from django.shortcuts import render
from .models import Category

def index(request):
    categorys = Category.objects.all()
    context = {
        'title': 'Блог',
        'categorys' : categorys
    }
    return render(request, 'blog/index.html', context)