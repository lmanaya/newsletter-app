from django.urls import path
from rest_framework import routers
from .viewsets import (
    NewsletterEmailViewSet,
    ImageUploadViewSet,
    DocumentUploadViewSet
)

router = routers.SimpleRouter()
router.register(r"newsletters", NewsletterEmailViewSet)
router.register(r"images", ImageUploadViewSet)
router.register(r"documents", DocumentUploadViewSet)

urlpatterns = []

urlpatterns += router.urls
