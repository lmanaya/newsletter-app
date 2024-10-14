from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import Newsletter, Subscriber
from .subscription import SubscriptionService

class NewsletterSerializer(serializers.ModelSerializer):
    """Serializer for creating newsletters."""
    class Meta:
        model = Newsletter
        fields = ["id", "name", "description", "call_to_action_text"]

class NewsletterListSerializer(serializers.ModelSerializer):
    """Serializer for listing newsletters."""
    class Meta:
        model = Newsletter
        fields = ["id", "name"]

class SubscriberSerializer(serializers.ModelSerializer):
    """Serializer for retrieve a subscriber."""
    newsletters = NewsletterListSerializer(many=True)

    class Meta:
        model = Subscriber
        fields = ["id", "email", "newsletters"]

class SubscriberListSerializer(serializers.ModelSerializer):
    """Serializer for listing subscribers."""
    class Meta:
        model = Subscriber
        fields = ["id", "email"]

class SubscribeSerializer(serializers.Serializer):
    """Serializer for subscribe to a newsletter."""
    email = serializers.EmailField()
    newsletter = serializers.PrimaryKeyRelatedField(
        queryset=Newsletter.objects.all(),
        write_only=True
    )
    newsletters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        subscriber = SubscriptionService.subscribe(**validated_data)
        if not subscriber:
            raise serializers.ValidationError(_("Email is already subscriber to this newsletter."))
        return subscriber

class UnsubscribeSerializer(serializers.Serializer):
    """Serializer for unsubscribe from a newsletter."""
    unsubscribe_token = serializers.UUIDField()
    newsletter = serializers.PrimaryKeyRelatedField(
        queryset=Newsletter.objects.all(),
        write_only=True,
        required=False
    )
    newsletters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        subscriber = SubscriptionService.unsubscribe(**validated_data)
        if not subscriber:
            raise serializers.ValidationError(
                _("Email does not exist or it is not subscriber to this newsletter.")
            )
        return subscriber
