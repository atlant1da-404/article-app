from django.db import models

from django.contrib.auth.models import User


class News(models.Model):
    """Схема-Модель новостей"""

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание статьи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор статьи')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления статьи')


    def __str__(self) -> str:
        return self.title
