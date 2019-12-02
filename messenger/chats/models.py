from django.db import models
from user_profile.models import User
from django.utils import timezone


class Chat(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        default='Unnamed Chat', verbose_name='Название чата')
    is_group_chat = models.BooleanField(verbose_name='Групповой')
    topic = models.CharField(max_length=128, verbose_name='Тема чата')
    host = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Создатель чата')
    last_message = models.ForeignKey(
        'message.Message',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Последнее сообщение',
        related_name='+')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'



