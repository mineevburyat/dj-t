from django.contrib import admin
from django.db import models
from .models import Category, Post
from markdownx.admin import MarkdownxModelAdmin
from tinymce.widgets import TinyMCE


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'watched', 'category', 'published')
    list_editable = ('published',)
    list_filter = ('category', 'published')
    readonly_fields = ('watched',)
    list_display_links = ('title', )
    formfield_overrides = {
  models.TextField: {'widget': TinyMCE()}
  }
    