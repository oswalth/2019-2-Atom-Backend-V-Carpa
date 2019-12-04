from django.db import models
from chats.models import Chat
from user_profile.models import User
from django.utils import timezone

class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Чат сообщения',
        related_name='messages_chat')
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Отправитель',
        related_name='messages_sender')
    content = models.TextField(verbose_name='Содержимое')
    added_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата отправки')

    def __str__(self):
        return '{} at {}'.format(self.content, self.added_at)

    class Meta():
        ordering = ('-added_at',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
