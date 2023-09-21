from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Subscription
from materials.serializers import CourseSerializer
from materials.services.permissions import IsOwner, IsStaff
from materials.paginators import CoursePaginator
from materials.tasks import send_emails_update_course


class CourseViewSet(viewsets.ModelViewSet):
    """Просмотр курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        """Права доступа"""
        if self.action == 'retrieve':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated | IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'list':
            permission_classes = [IsOwner | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
        list_obj = Subscription.objects.filter(course=self.get_object())
        emails = [obj.user.email for obj in list_obj]
        send_emails_update_course.delay(self.get_object().id, emails)