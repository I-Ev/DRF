from rest_framework import serializers

from payment.models import Payment
from payment.stripe_services import retrieve_payment_intent


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentRetrieveAPIView(serializers.ModelSerializer):
    """Просмотр платежа"""
    stripe_payment_info = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = "__all__"

    def get_stripe_payment_info(self, obj):
        stripe_payment_info = retrieve_payment_intent(obj.stripe_id)
        return stripe_payment_info