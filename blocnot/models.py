from django.db import models
from django.contrib.auth.models import User  # <--- 1. Импортируем модель Пользователя



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    # text — теперь обязательное поле
    text = models.TextField(verbose_name="Текст заметки")

    # auto_now_add — ставится один раз при создании
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    # auto_now — обновляется КАЖДЫЙ РАЗ при сохранении
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-updated_at']  # Сверху будут самые свежие (недавно отредактированные)