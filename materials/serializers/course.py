from rest_framework import serializers

from materials.models import Course, Subscription
from materials.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, source='lesson', read_only=True)
    lessons_count = serializers.SerializerMethodField(read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson.count()

    def get_is_subscribed(self, instance):
        """Проверка подписки"""
        request = self.context.get('request')
        subscription = Subscription.objects.filter(course=instance.pk, user=request.user).exists()
        if subscription:
            return True
        return False
