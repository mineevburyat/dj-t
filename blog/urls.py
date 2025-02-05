from django.urls import path
from .views import (index, detail_post, posts_by_category, 
                    add_post, update_post, DeletePostView)

app_name =  'blog'
urlpatterns = [
    path('', index, name='index'),
    path('add/', add_post, name='add_post'),
    path('post/<int:pk>', detail_post, name='detail_post'),
    path('category/<int:pk>', posts_by_category, name='filtered_posts'),
    path('update/<int:pk>', update_post, name='update_post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete_post')
]