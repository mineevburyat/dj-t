from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def login_user(request):
    print(request.POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                logout(request)
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                messages.success(request, 'успешно аутентифицирован')
                # if form.next:
                #     return redirect(next)
                return redirect(reverse('blog:index'))
            else:
                messages.error(request, 'Неверный логин или пароль')
    form = LoginForm()
    # form.next. = request.GET.get('next')
    context = {
        'title': "аутентификация",
        'form': form,
        }
    
    return render(request, 'userauth/login.html', context)
    


def logout_user(request):
    logout(request)
    return redirect(reverse('blog:index'))