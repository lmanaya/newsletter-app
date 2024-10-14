from rest_framework import viewsets, mixins
from .models import NewsletterEmail, ImageUpload, DocumentUpload
from .serializers import (
    ImageUploadSerializer,
    DocumentUploadSerializer
)

class ImageUploadViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
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
    viewsets.GenericViewSet
):
    """
    ViewSet for uploaded document create(), retrieve() and destroy() actions
    """
    queryset = DocumentUpload.objects.all()
    serializer_class = DocumentUploadSerializer
