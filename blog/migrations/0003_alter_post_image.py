# Generated by Django 5.1.5 on 2025-01-31 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog', verbose_name='Картинка'),
        ),
    ]
