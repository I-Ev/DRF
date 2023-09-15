from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet
from materials.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonDetailAPIView
from materials.views.subscription import SubscriptionListAPIView, SubscriptionCreateAPIView, SubscriptionDeleteAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lessons-list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscriptions_list'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('subscription/delete/<int:pk>/', SubscriptionDeleteAPIView.as_view(), name='subscription-delete'),
] + router.urls
