from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .mixins import NewsletterEmailValidationMixin
from .models import NewsletterEmail, ImageUpload, DocumentUpload
from newsletters.models import Newsletter, Subscriber

class NewsletterEmailSerializer(serializers.ModelSerializer):
    """ Serializer for listing or retrieving newsletter emails. """
    class Meta:
        model = NewsletterEmail
        fields = "__all__"

class NewsletterEmailCreateSerializer(
    NewsletterEmailValidationMixin, serializers.ModelSerializer
):
    """ Serializer for creating newsletter emails. """
    newsletter = serializers.PrimaryKeyRelatedField(
        queryset=Newsletter.objects.all()
    )

    class Meta:
        model = NewsletterEmail
        fields = "__all__"

class NewsletterEmailUpdateSerializer(
    NewsletterEmailValidationMixin, serializers.ModelSerializer
):
    """ Serializer for updating newsletter emails. """
    class Meta:
        model = NewsletterEmail
        fields = "__all__"

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = "__all__"

class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentUpload
        fields = "__all__"
