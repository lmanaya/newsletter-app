from typing import Optional
from .models import NewsletterEmail
from .tasks import send_newsletter_email_task
from django.template.loader import render_to_string
from newsletters.models import Subscriber
from os import environ, path, remove
from django.conf import settings
from django.template import Template, Context
from .constants import SENDED_STATUS

class EmailService:
    @staticmethod
    def get_newsletter_email_html_content(
        subscriber: Subscriber,
        body: Optional[str] = None,
        title: Optional[str] = None,
        content: Optional[str] = None
    ) -> str:
        """
        Generate HTML content for the newsletter email.

        Args:
            subscriber (Subscriber): The subscriber te recieve the email.
            body (Optional[str]): The HTML body of the email template.
            title (Optional[str]): The title of email when the body is not provided.
            content (Optional[str]): The content of email when the body is not provided.

        Returns:
            str: The HTML content for the newsletter email specific for a subscriber
        """

        unsubscribe_url = f"{environ.get('WEB_BASE_URL')}/unsubscribe?token={subscriber.unsubscribe_token}"

        if not body:
            return render_to_string('default.html', {
                "title": title,
                "content": content,
                "unsubscribe_url": unsubscribe_url
            })

        template = Template(body)
        context = Context({
            'unsubscribe_url': unsubscribe_url
        })
        return template.render(context)

    @staticmethod
    def mark_newsletter_email_as_sent(newsletterEmail: NewsletterEmail) -> None:
        """
        Mark the newsletter email as sent.

        Args:
            newsletterEmail (NewsletterEmail): The newsletter email to update.
        """
        newsletterEmail.status = SENDED_STATUS
        newsletterEmail.save()

    @staticmethod
    def send_newsletter_email(newsletterEmail: NewsletterEmail) -> None:
        """
        Send newsletter email to subscribers.

        Args:
            newsletterEmail (NewsletterEmail): The newsletter email to send.
        """
        for subscriber in newsletterEmail.subscribers.all():
            html_content = EmailService.get_newsletter_email_html_content(
                subscriber=subscriber,
                body=newsletterEmail.body,
                title=newsletterEmail.title,
                content=newsletterEmail.content
            )
            send_newsletter_email_task.delay(
                newsletter_email_pk=newsletterEmail.pk,
                subject=newsletterEmail.subject,
                subscriber=subscriber.email,
                html_content=html_content
            )

        EmailService.mark_newsletter_email_as_sent(newsletterEmail)
