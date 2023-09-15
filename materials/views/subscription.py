from rest_framework import generics

from materials.models import Lesson
from materials.serializers.subscription import SubscriptionSerializer
from materials.services.permissions import IsOwner, IsStaff


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Создание подписки"""
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        new_subscribe = serializer.save()
        new_subscribe.user = self.request.user
        new_subscribe.save()


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStaff]


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    """Удаление подписки"""
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStaff]