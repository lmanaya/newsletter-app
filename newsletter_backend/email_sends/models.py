from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import STATUS_EMAIL_CHOICES, PENDING_STATUS
from newsletters.models import Newsletter, Subscriber

class BaseAbstractDocument(models.Model):
    """" Abstract model of documents """
    name = models.CharField(_("name"), max_length=255)
    uploaded_at = models.DateTimeField(_("uploaded at"), auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        abstract = True

class FileDocument(BaseAbstractDocument):
    """" Model of file documents (PDF files) """
    file = models.FileField(_("file"), upload_to='uploads/documents/')

    class Meta:
        verbose_name = _("document")
        verbose_name_plural = _("documents")

class ImageDocument(BaseAbstractDocument):
    """" Model of images documents (PNG files) """
    file = models.ImageField(_("file"), upload_to='uploads/images/')

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")

class EmailTemplate(models.Model):
    """" Model of email templates for newsletter sendings """
    subject = models.CharField(_("subject"), max_length=255)
    body = models.TextField(_("email body"))
    attached_files = models.ManyToManyField(
        "FileDocument",
        blank=True
    )
    attached_images = models.ManyToManyField(
        "ImageDocument",
        blank=True
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.subject}"

    class Meta:
        verbose_name = _("email template")
        verbose_name_plural = _("email templates")

class EmailSend(models.Model):
    """" Model for tracking email sendings of newsletters """
    email_template = models.ForeignKey(
        EmailTemplate,
        on_delete=models.SET_NULL,
        null=True
    )
    newsletter = models.ForeignKey(
        Newsletter,
        on_delete=models.SET_NULL,
        null=True
    )
    subscriber = models.ForeignKey(
        Subscriber,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        _("status"),
        choices=STATUS_EMAIL_CHOICES,
        default=PENDING_STATUS,
        max_length=10
    )
    sent_at = models.DateTimeField(_("send at"), blank=True, null=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        template = self.email_template.subject if self.email_template else "No Template"
        subscriber = self.subscriber.email if self.subscriber else "No Subscriber"
        return f"{self.pk} - {template} - {subscriber}"

    class Meta:
        verbose_name = _("email send")
        verbose_name_plural = _("email sends")
