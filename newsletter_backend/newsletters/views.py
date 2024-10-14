from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from .models import Subscriber
from .serializers import (
    SubscribeSerializer,
    UnsubscribeSerializer
)

class SubscribeView(generics.CreateAPIView):
    """
    View for subscribe to a newsletter.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnsubscribeView(generics.CreateAPIView):
    """
    View for unsubscribe from a newsletter.
    """
    queryset = Subscriber.objects.all()
    serializer_class = UnsubscribeSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
