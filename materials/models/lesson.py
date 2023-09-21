from django.conf import settings
from django.db import models

from materials.models import Course
from users.models import NULLABLE


class Lesson(models.Model):
    """Инфо об уроке"""
    title = models.CharField(unique=True, max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    preview = models.ImageField(upload_to='materials/lessons/preview', verbose_name='Превью', **NULLABLE)
    video_link = models.CharField(max_length=150, verbose_name="Ссылка на видео", **NULLABLE)

    course = models.ForeignKey(Course, verbose_name="курс", **NULLABLE, on_delete=models.CASCADE,
                               related_name="lesson")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.CASCADE)

    lesson_price = models.IntegerField(verbose_name="Цена", default=1000)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
