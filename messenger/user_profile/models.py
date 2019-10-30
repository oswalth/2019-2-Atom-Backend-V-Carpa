from django.db import models
from django.utils import timezone
# from chats.models import Chats, Message


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128, blank=False)
    nick = models.CharField(max_length=32, blank=False)
    avatar = models.CharField(max_length=128)
    status = models.CharField(max_length=64, blank=False, default='Online')
    last_seen = models.DateTimeField(default=timezone.now())
    created_date = models.DateTimeField(default=timezone.now())


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.SET_NULL,
        null=True)
    # new_messages =
    last_read_message = models.ForeignKey(
        'chats.Message', on_delete=models.SET_NULL, null=True)
