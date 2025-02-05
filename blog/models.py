'''
https://neutronx.github.io/django-markdownx/translations/
https://habr.com/ru/articles/689106/
'''

from django.db import models
# from markdownx.models import MarkdownxField
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=65)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:filtered_posts', kwargs={'pk': self.pk})
    
    def get_choise_tupl(self):
        pass

class Post(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=165)
    content = HTMLField(verbose_name='Текст',)
    created = models.DateTimeField(verbose_name='Создан',
                                   auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен',
                                   auto_now=True)
    published = models.BooleanField(verbose_name='Активность',
                                    default=False)
    watched = models.IntegerField(verbose_name='Просмотрено',
                                  default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='posts',
                                 verbose_name='Категория',)
    image = models.ImageField(verbose_name='Картинка',
                              upload_to='blog',
                              blank=True)
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.title} ({self.category})"
    
    def get_absolute_url(self):
        return reverse('blog:detail_post', kwargs={'pk': self.pk})