from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import STATUS_EMAIL_CHOICES, PENDING_STATUS
from newsletters.models import Newsletter, Subscriber

class AbstractUpload(models.Model):
    """" Abstract model for uploaded files. """
    name = models.CharField(_("name"), max_length=255)
    uploaded_at = models.DateTimeField(_("uploaded at"), auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        abstract = True

class DocumentUpload(AbstractUpload):
    """" Model for uploaded documents (PDF files). """
    file = models.FileField(_("file"), upload_to='uploads/documents/')

    class Meta:
        verbose_name = _("document")
        verbose_name_plural = _("documents")

class ImageUpload(AbstractUpload):
    """" Model for uploaded images. (PNG files) """
    file = models.ImageField(_("file"), upload_to='uploads/images/')

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")

class AbstractEmail(models.Model):
    """" Abstract model for email tracking. """
    subject = models.CharField(_("subject"), max_length=255)
    title = models.CharField(_("title"), max_length=100, blank=True, null=True)
    content = models.TextField(_("content"), blank=True, null=True)
    body = models.TextField(_("body"), blank=True, null=True)
    status = models.CharField(
        _("status"),
        choices=STATUS_EMAIL_CHOICES,
        default=PENDING_STATUS,
        max_length=10
    )
    sent_at = models.DateTimeField(_("send at"), blank=True, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.subject}"

    class Meta:
        abstract = True

class NewsletterEmail(AbstractEmail):
    """" Model for tracking newsletter emails. """
    newsletter = models.ForeignKey(
        Newsletter,
        on_delete=models.SET_NULL,
        null=True,
        related_name='newsletter_emails'
    )
    subscribers = models.ManyToManyField(
        Subscriber,
        blank=True,
        related_name='newsletter_emails'
    )
    attached_documents = models.ManyToManyField(
        "DocumentUpload",
        blank=True,
        related_name='newsletter_emails'
    )
    attached_images = models.ManyToManyField(
        "ImageUpload",
        blank=True,
        related_name='newsletter_emails'
    )

    class Meta:
        verbose_name = _("newsletter email")
        verbose_name_plural = _("newsletter emails")
