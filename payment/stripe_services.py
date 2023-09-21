import stripe

from config import settings
from materials.models import Course, Lesson

stripe.api_key = settings.STRIPE_API_KEY


def create_payment_intent(amount):
    """
    Создаем намерение на платеж по курсу или уроку, в ответ получаем json по созданного намерения
    """
    json_response = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    # возвращаем json результат созданного намерения платежа
    return json_response

def retrieve_payment_intent(payment_intent_id):
    """
    Получаем по id сведения о PaymentIntent, который был создан ранее
    """
    json_response = stripe.PaymentIntent.retrieve(
        str(payment_intent_id),
    )
    return json_response
