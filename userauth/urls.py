from django.urls import path

from .views import login_user, logout_user, LoginUser
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_pass/', auth_views.PasswordChangeView.as_view())
]