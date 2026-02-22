from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(actor, recipient, verb, target):
    if actor == recipient:
        return  # Avoid self-notifications

    Notification.objects.create(
        actor=actor,
        recipient=recipient,
        verb=verb,
        content_type=ContentType.objects.get_for_model(target),
        object_id=target.id
    )