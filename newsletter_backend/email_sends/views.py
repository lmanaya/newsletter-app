from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendNewsletterEmailSerializer
from .emails import EmailService

class SendNewsletterEmailView(generics.GenericAPIView):
    """
    View for sending newsletter email to subscribers.
    """
    serializer_class = SendNewsletterEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        newsletter_email = serializer.validated_data.get("newsletter_email")
        try:
            EmailService.send_newsletter_email(newsletter_email)
            return Response(
                { "success": "Newsletter email sended successfully!" },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                { "error": e },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
