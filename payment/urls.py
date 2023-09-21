from django.urls import path

from payment.apps import PaymentConfig
from payment.views import (PaymentListAPIView, PaymentCreateAPIView, PaymantRetrieveAPIView)

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('retrieve/<int:pk>/', PaymantRetrieveAPIView.as_view(), name='payment_view'),

]
