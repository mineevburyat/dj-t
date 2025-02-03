from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

# Create your views here.


def login_user(request):
    context = {}
    return render(request, 'userauth/login.html', context)

class LoginUser(auth_views.LoginView):
    next_page = reverse_lazy('blog:index')
    template_name = 'userauth/login.html'

def logout_user(request):
    auth_views.logout(request)
    return redirect(reverse('blog:index'))