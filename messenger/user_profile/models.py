from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# from chats.models import Chats, Message


# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=128)

    def __str__(self):
        return(' '.join([self.first_name, self.last_name]))

    class Meta:
        ordering = ('date_joined',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.CASCADE,
        null=True)
    # new_messages =
    last_read_message = models.ForeignKey(
        'chats.Message', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чатов'