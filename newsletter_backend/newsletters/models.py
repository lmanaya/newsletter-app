import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Newsletter(models.Model):
    """
    Newsletter administration model
    """
    name = models.CharField(_("name"), max_length=100)
    description = models.CharField(_("description"), max_length=255)
    call_to_action_text = models.CharField(_("call to action text"), max_length=255)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = _("newsletter")
        verbose_name_plural = _("newsletters")

class Subscriber(models.Model):
    """
    Newsletter subscriber model
    """
    email = models.EmailField(_("email"), unique=True)
    newsletters = models.ManyToManyField('Newsletter', blank=True, related_name='subscribers')
    unsubscribe_token = models.UUIDField(
        _("unsubscribe token"),
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    @property
    def subscribed_to_newsletters(self):
        return self.newsletters.exists()

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing it.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name.lower() + "@" + domain_part.lower()
        return email

    def clean(self):
        super().clean()
        self.email = self.normalize_email(self.email)

    def __str__(self):
        return f"{self.pk} - {self.email}"

    class Meta:
        verbose_name = _("subscriber")
        verbose_name_plural = _("subscribers")
