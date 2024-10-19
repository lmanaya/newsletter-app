from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Newsletter, Subscriber
from .serializers import (
    NewsletterSerializer,
    NewsletterListSerializer,
    SubscriberSerializer,
    SubscriberListSerializer
)

class NewsletterViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet for newsletters create(), retrieve() and list() actions
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return NewsletterListSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action == "list":
            return []
        return super().get_permissions()

class SubscriberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for subscribers retrieve() and list() actions
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['newsletters']
    search_fields = ['email']

    def get_serializer_class(self):
        if self.action == "list":
            return SubscriberListSerializer

        return self.serializer_class
