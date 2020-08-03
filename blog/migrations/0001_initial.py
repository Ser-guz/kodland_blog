# Generated by Django 3.0.9 on 2020-08-03 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, max_length=6050, null=True, verbose_name='Текст публикации')),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='Опубликовано')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['-publish_date', '-timestamp', '-updated'],
            },
        ),
    ]
