from __future__ import absolute_import,unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def add(x,y):
    return x + y

@shared_task
def send_forget_password_mail(email_id,password):
    send_mail(
                subject='Studybud Password Reset',
                message=f'This is you newly generated password {password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email_id])