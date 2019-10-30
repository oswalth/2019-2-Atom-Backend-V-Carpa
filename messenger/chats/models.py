from django.db import models
from user_profile.models import User
from django.utils import timezone
# from stickers.models import Stickers


# Create your models here.
class Chat(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        default='Unnamed Chat')
    # sticker = models.ForeignKey(Stickers, on_delete=models.SET_NULL, null=True, related_name='chats')
    is_group_chat = models.BooleanField()
    topic = models.CharField(max_length=128)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # last_message =


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    added_at = models.DateTimeField(default=timezone.now())


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    # sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    attachment_type = models.CharField(max_length=16, blank=False)
    url = models.CharField(max_length=128)
