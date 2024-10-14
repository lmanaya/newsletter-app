from django.urls import path
from rest_framework import routers
from .views import SendNewsletterEmailView
from .viewsets import (
    NewsletterEmailViewSet,
    ImageUploadViewSet,
    DocumentUploadViewSet
)

router = routers.SimpleRouter()
router.register(r"newsletters", NewsletterEmailViewSet)
router.register(r"images", ImageUploadViewSet)
router.register(r"documents", DocumentUploadViewSet)

urlpatterns = [
    path("send-newsletter/", SendNewsletterEmailView.as_view(), name="send_newsletter"),
]

urlpatterns += router.urls

"""
URL configuration for the email sends app.

This module defines the URL patterns for the following actions:
- Newsletter email management actios.
- Uploading of image and documents attached to emails.
- Sending newsletter emails to subscribers.
"""
