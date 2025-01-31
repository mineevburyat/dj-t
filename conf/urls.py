from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

urlpatterns = [
    path('', include('blog.urls')),
    path('grappelli/', include('grappelli.urls')), 
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('tinymce/', include('tinymce.urls')),
] + debug_toolbar_urls() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
