from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    image = models.ImageField(u"Изображение", upload_to='images/', blank=True, null=True)
    slug = models.SlugField(u"Слаг", unique=True)
    title = models.CharField(u"Заголовок", max_length=50)
    content = models.TextField(u"Текст публикации", null=True, blank=True, max_length=6050)
    publish_date = models.DateTimeField(u"Опубликовано", auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(u"Создано", auto_now_add=True)
    updated = models.DateTimeField(u"Обновлено", auto_now=True)

    class Meta:
        ordering = ['-publish_date', '-timestamp', '-updated']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"