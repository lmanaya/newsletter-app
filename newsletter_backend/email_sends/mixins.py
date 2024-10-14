from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .constants import PENDING_STATUS, SENDED_STATUS
from newsletters.models import Subscriber

class NewsletterEmailValidationMixin:
    """
    Mixin for validating NewsletterEmail instances.
    """

    def validate(self, attrs):
        """
        Validate the incoming data for the NewsletterEmail instance.

        - Prevent updates to emails with status 'SENDED'.
        - Ensure only one file (document or image) can be attached.
        - If no subscribers are provided, fetch them based on the newsletter.
        - Validate that subscribers list is not empty.
        - Validate that title or content is required if the body is empty.
        - Ensure status is 'PENDING' for new instances.

        Args:
            attrs (dict): The data being validated.

        Returns:
            dict: The validated data.
        """
        errors = {}
        instance = getattr(self, "instance", None)

        self._validate_status(instance)

        self._validate_attachments(attrs, instance)

        self._validate_subscribers(attrs, instance)

        self._validate_content(attrs, instance, errors)

        self._validate_initial_status(attrs, instance, errors)

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    def _validate_status(self, instance):
        """ Prevent updates to emails with status 'SENDED'. """
        if instance and instance.status == SENDED_STATUS:
            raise serializers.ValidationError(
                _("This newsletter email cannot be updated.")
            )

    def _validate_attachments(self, attrs, instance):
        """ Validate that only one file is attached. """
        attached_documents = attrs.get(
            "attached_documents",
            instance.attached_documents.all() if instance else []
        )
        attached_images = attrs.get(
            "attached_images",
            instance.attached_images.all() if instance else []
        )

        if len(attached_documents) + len(attached_images) > 1:
            raise serializers.ValidationError(
                _("Only one file can be attached.")
            )

    def _validate_subscribers(self, attrs, instance):
        """ Ensure the subscribers field is not empty or None. """
        subscribers = attrs.get(
            "subscribers",
            instance.subscribers.all() if instance else []
        )
        newsletter = attrs.get(
            "newsletter",
            instance.newsletter if instance else None
        )

        if not subscribers:
            attrs["subscribers"] = Subscriber.objects.filter(
                newsletters__in=[newsletter]
            )

        if subscribers and len(subscribers) == 0:
            raise serializers.ValidationError(
                {"subscribers": [_("This field cannot be empty.")]}
            )


    def _validate_content(self, attrs, instance, errors):
        """
        Validate that title or content is required if the body is not provided.
        """
        title = attrs.get("title", instance.title if instance else None)
        content = attrs.get("content", instance.content if instance else None)
        body = attrs.get("body", None)

        if not body:
            if not title:
                errors["title"] = [_("This field is required.")]
            if not content:
                errors["content"] = [_("This field is required.")]

    def _validate_initial_status(self, attrs, instance, errors):
        """ Validate  status is 'PENDING' for new instances. """
        status = attrs.get("status", None)
        if not instance and status and status != PENDING_STATUS:
            errors["status"] = [_('This field value must be "pending".')]
