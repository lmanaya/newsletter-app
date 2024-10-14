from django.conf.global_settings import EMAIL_HOST_USER
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_email_task

class SendEmailView(views.APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        send_email_task(
            subject="Test email sending",
            message="This is the testing for send emails with celery",
            from_email=EMAIL_HOST_USER,
            recipient_list=["liyeira@elmundoseo.com"]
        )

        return Response({ "success": "Email sending successfully!" }, status=status.HTTP_200_OK)
