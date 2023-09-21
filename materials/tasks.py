from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course


@shared_task
def send_emails_update_course(course_id, users_emails_list):
    course_name = Course.objects.get(pk=course_id).title
    email_list= users_emails_list
    from_email = settings.EMAIL_HOST_USER
    subject = f'Мы обновили курс {course_name}'
    message = 'Уважаемый клиент! Мы обновили курс, на который вы записались. Теперь он стал еще интреснее!'


    for email in email_list:
        try:
            send_mail(subject, message, from_email, [email], fail_silently=False)
        except Exception as e:
            print(f"ошибка при отправке сообщения на email {email}: {e}")
