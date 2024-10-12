from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_notification_task

@api_view(['POST'])
def trigger_notification(request):
    user_id = request.data.get('user_id')
    message = request.data.get('message')

    # Save notification to the database (optional)
    # Notification.objects.create(user_id=user_id, message=message)

    # Trigger the Celery task
    send_notification_task.delay(user_id, message)

    return Response({'status': 'Notification sent'})
