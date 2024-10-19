from rest_framework import viewsets, mixins
from .models import NewsletterEmail, ImageUpload, DocumentUpload
from .serializers import (
    NewsletterEmailSerializer,
    NewsletterEmailCreateSerializer,
    NewsletterEmailUpdateSerializer,
    ImageUploadSerializer,
    DocumentUploadSerializer
)

class NewsletterEmailViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet for newsletter email create(), retrieve() and list() actions
    """
    queryset = NewsletterEmail.objects.all()
    serializer_class = NewsletterEmailSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return NewsletterEmailCreateSerializer
        if self.action == "partial_update":
            return NewsletterEmailUpdateSerializer

        return self.serializer_class

class ImageUploadViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet for uploaded image create(), retrieve() and destroy() actions
    """
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

class DocumentUploadViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet for uploaded document create(), retrieve() and destroy() actions
    """
    queryset = DocumentUpload.objects.all()
    serializer_class = DocumentUploadSerializer
