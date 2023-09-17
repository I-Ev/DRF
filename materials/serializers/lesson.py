from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Lesson, Course
from materials.validators.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='id', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='video_link')]