from django.urls import path
from rest_framework import routers
from .views import SendNewsletterView
from .viewsets import (
    ImageUploadViewSet,
    DocumentUploadViewSet
)

router = routers.SimpleRouter()
router.register(r"images", ImageUploadViewSet)
router.register(r"documents", DocumentUploadViewSet)

urlpatterns = []

urlpatterns += router.urls
