from django.urls import path
from .views import index, detail_post, posts_by_category

app_name =  'blog'
urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', detail_post, name='detail_post'),
    path('category/<int:pk>', posts_by_category, name='filtered_posts')
]