from rest_framework import serializers


class LinkValidator:
    """Валидатор проверяет корректность ссылки на видео"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Можно добавлять только сслыки на youtube"""
        video_link = value.get('video_link')
        if video_link != None and 'www.youtube' not in video_link:
            raise serializers.ValidationError('Допустимы ссылки только на youtube')