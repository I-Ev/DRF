from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.stripe_services import  create_payment_intent


class PaymentListAPIView(generics.CreateAPIView):
    """Просмотр платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Изменение последовательности
    ordering_fields = ('date_of_payment',)
    # фильтрация по полям
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')

class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа для оплаты урока или курса"""
    serializer_class = PaymentSerializer
    def perform_create(self, serializer):
        new_payment = serializer.save()
        stripe_payment_intent = create_payment_intent(new_payment.payment_amount)
        new_payment.user = self.request.user
        new_payment.stripe_id = stripe_payment_intent['id']

        new_payment.save()




class PaymantRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer