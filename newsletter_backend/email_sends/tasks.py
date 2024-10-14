from django.conf.global_settings import EMAIL_HOST_USER
from typing import Optional, List
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from newsletters.models import Subscriber
from django.db.models import QuerySet
from .models import NewsletterEmail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email_task(
    subject: str,
    recipients: List[str],
    html_content: str,
    from_email: Optional[str] = EMAIL_HOST_USER
):
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        recipients
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

@shared_task
def send_newsletter_email_task(
    newsletter_email_pk: int,
    subject: str,
    subscriber: str,
    html_content: str
):
    try:
        logger.info(f"Sending newsletter email {newsletter_email_pk} to {subscriber}")
        send_email_task(
            subject=subject,
            recipients=[subscriber],
            html_content=html_content
        )
    except Exception as e:
        logger.error(f"Error sending newsletter email {newsletter_email_pk} to {subscriber}: {e}")
