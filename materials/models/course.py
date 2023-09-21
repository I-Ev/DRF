from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """Информация о курсе"""
    title = models.CharField(max_length=100, unique=True, verbose_name=' Название')
    preview = models.ImageField(upload_to='materials/courses/preview', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.CASCADE)
    course_price = models.IntegerField(verbose_name='Цена', default=1000)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
