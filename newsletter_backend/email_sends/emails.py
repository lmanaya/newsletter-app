from typing import Optional
from .models import NewsletterEmail
from .tasks import send_newsletter_email_task
from django.template.loader import render_to_string
from newsletters.models import Subscriber, Newsletter
from os import environ
from django.template import Template, Context
from .constants import SENDED_STATUS
import mimetypes

class EmailService:
    @staticmethod
    def get_newsletter_email_html_content(
        newsletter: Newsletter,
        subscriber: Subscriber,
        body: Optional[str] = None,
        title: Optional[str] = None,
        content: Optional[str] = None,
    ) -> str:
        """
        Generate HTML content for the newsletter email.

        Args:
            newsletter (Newsletter): The newsletter from the email.
            subscriber (Subscriber): The subscriber to recieve the email.
            body (Optional[str]): The HTML body of the email template.
            title (Optional[str]): The title of email when the body is not provided.
            content (Optional[str]): The content of email when the body is not provided.

        Returns:
            str: The HTML content for the newsletter email specific for a subscriber
        """

        unsubscribe_url = f"{environ.get('WEB_BASE_URL')}/unsubscribe?token={subscriber.unsubscribe_token}&newsletter={newsletter.id}"

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
    def mark_newsletter_email_as_sent(newsletter_email: NewsletterEmail) -> None:
        """
        Mark the newsletter email as sent.

        Args:
            newsletter_email (NewsletterEmail): The newsletter email to update.
        """
        newsletter_email.status = SENDED_STATUS
        newsletter_email.save()

    @staticmethod
    def send_newsletter_email(newsletter_email: NewsletterEmail) -> None:
        """
        Send newsletter email to subscribers.

        Args:
            newsletter_email (NewsletterEmail): The newsletter email to send.
        """
        for subscriber in newsletter_email.subscribers.all():
            html_content = EmailService.get_newsletter_email_html_content(
                newsletter=newsletter_email.newsletter,
                subscriber=subscriber,
                body=newsletter_email.body,
                title=newsletter_email.title,
                content=newsletter_email.content
            )

            attached_files_info = EmailService.set_attached_files_info(newsletter_email)

            send_newsletter_email_task.delay(
                newsletter_email_pk=newsletter_email.pk,
                subject=newsletter_email.subject,
                subscriber=subscriber.email,
                html_content=html_content,
                attached_files_info=attached_files_info,
            )

        EmailService.mark_newsletter_email_as_sent(newsletter_email)

    @staticmethod
    def set_attached_files_info(newsletter_email: NewsletterEmail) -> list:
        """
        Set attached files info for newsletter email.

        Args:
            newsletter_email (NewsletterEmail): The newsletter email to get de attached files.
        """
        attached_files_info = []

        documents = [ document for document in newsletter_email.attached_documents.all() ] \
            + [ image for image in newsletter_email.attached_images.all() ]

        for document in documents:
            content_type, _ = mimetypes.guess_type(document.file.path)
            attached_files_info.append({
                "name": document.name,
                "url": document.file.path,
                "content_type": content_type
            })

        return attached_files_info
