from django.urls import path
from rest_framework import routers
from .views import SubscribeView, UnsubscribeView
from .viewsets import NewsletterViewSet, SubscriberViewSet

router = routers.SimpleRouter()
router.register(r"newsletters", NewsletterViewSet)
router.register(r"subscribers", SubscriberViewSet)

urlpatterns = [
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("unsubscribe/", UnsubscribeView.as_view(), name="unsubscribe"),
]

urlpatterns += router.urls

"""
URL configuration for the newsletters app.

This module defines the URL patterns for subscribing, unsubscribing,
and managing newsletters and subscribers.
"""
