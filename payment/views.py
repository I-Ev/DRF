from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListAPIView(generics.CreateAPIView):
    """Просмотр платежей"""
    queryset = Payment.objects.all()
    serializer = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Изменение последовательности
    ordering_fields = ('date_of_payment',)
    # фильтрация по полям
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')