from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from .views import welcome

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('welcome/', welcome, name="welcome"),
    path('grappelli/', include('grappelli.urls')), 
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('pools/', include('pools.urls', namespace='pools')),
    path('user/', include('userauth.urls', namespace='user'))
] + debug_toolbar_urls() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
