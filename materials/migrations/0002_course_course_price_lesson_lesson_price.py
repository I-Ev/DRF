# Generated by Django 4.2.4 on 2023-09-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_price',
            field=models.IntegerField(default=1000, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_price',
            field=models.IntegerField(default=1000, verbose_name='Цена'),
        ),
    ]