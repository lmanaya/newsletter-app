from typing import Optional
from django.db.models import QuerySet
from .models import Subscriber, Newsletter

class SubscriptionService:
    @staticmethod
    def create_subscriber(email: str, newsletter: Newsletter) -> Subscriber:
        """
        Create de subscribers into database.

        Args:
            email (str): The email of the subscriber.
            newsletter (Newsletter): The newsletter to subscribe to.

        Returns:
            Subscriber: The created subscribe.
        """
        subscriber = Subscriber.objects.create(email=email)
        subscriber.newsletters.add(newsletter)
        return subscriber

    @staticmethod
    def existing_subscription(
        subscriber: Subscriber, newsletter: Newsletter
    ) -> bool:
        """
        Validate existing subscriber to specific newsletter.

        Args:
            subscriber (Subscriber): Subscriber to validate.
            newsletter (Newsletter): The newsletter which is subscribed.

        Returns:
            bool: True if the subscriber is already subscribed to the
                newsletter, False otherwise.
        """
        return subscriber.newsletters.all().filter(pk=newsletter.pk).exists()

    @staticmethod
    def subscribe_newsletter(
        subscriber: Subscriber, newsletter: Newsletter
    ) -> Subscriber:
        """
        Add a newsletter to the subscriber's newsletters list.

        Args:
            subscriber (Subscriber): The subscriber to add to the newsletter.
            newsletter (Newsletter): The newsletter to be added.

        Returns:
            Subscriber: The updated subscriber instance.
        """
        subscriber.newsletters.add(newsletter)
        return subscriber

    @staticmethod
    def unsubscribe_newsletter(
        subscriber: Subscriber, newsletter: Optional[Newsletter] = None
    ) -> Subscriber:
        """
        Remove a specific newsletter or all newsletters from the subscriber.

        Args:
            subscriber (Subscriber): The subscriber to update.
            newsletter (Optional[Newsletter]): The newsletter to be removed.
                If None, all newsletters will be removed.

        Returns:
            Subscriber: The updated subscriber instance.
        """
        if newsletter:
            subscriber.newsletters.remove(newsletter)
        else:
            subscriber.newsletters.clear()
        return subscriber

    @staticmethod
    def subscribe(email: str, newsletter: Newsletter) -> Optional[Subscriber]:
        """
        Subscribe to a newsletter.

        Args:
            email (str): The email of the subscriber.
            newsletter (Optional[Newsletter]): The specific newsletter to
                subscribe to.

        Returns:
            Optional[Subscriber]: The created or updated subscriber or None if
                it is already subscribed.
        """
        subscriber = Subscriber.objects.filter(email=email).first()
        if not subscriber:
            subscriber = SubscriptionService.create_subscriber(
                email=email, newsletter=newsletter
            )
            return subscriber

        if SubscriptionService.existing_subscription(
            subscriber=subscriber, newsletter=newsletter
        ):
            return None

        subscriber = SubscriptionService.subscribe_newsletter(
            subscriber=subscriber, newsletter=newsletter
        )

        return subscriber

    @staticmethod
    def unsubscribe(
        unsubscribe_token: str, newsletter: Optional[Newsletter] = None
    ) -> Optional[Subscriber]:
        """
        Unsubscribe from a newsletter.

        Args:
            unsubscribe_token (str): The token to identify the subscriber.
            newsletter (Optional[Newsletter]): The specific newsletter to
                unsubscribe from (optional).

        Returns:
            Optional[Subscriber]: The updated subscriber or None if not found.
        """
        subscriber = Subscriber.objects.filter(
            unsubscribe_token=unsubscribe_token
        ).first()
        if not subscriber:
            return None

        if newsletter and not SubscriptionService.existing_subscription(
            subscriber=subscriber, newsletter=newsletter
        ):
            return None

        subscriber = SubscriptionService.unsubscribe_newsletter(
            subscriber=subscriber, newsletter=newsletter
        )

        return subscriber
