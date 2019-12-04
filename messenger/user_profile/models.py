from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# from chats.models import Chats, Message


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/{1}'.format(instance.username, 'avatar')


class User(AbstractUser):
    avatar = models.ImageField(name='avatar', upload_to=user_directory_path, null=True, verbose_name='Аватар', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return(' '.join([self.first_name, self.last_name]))

    class Meta:
        ordering = ('date_joined',)
        verbose_name = ('Пользователь')
        verbose_name_plural = ('Пользователи')


class Member(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь',
        related_name='membership')
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.CASCADE,
        null=True, 
        verbose_name='Чат',
        related_name='membership')
    # new_messages =
    last_read_message = models.ForeignKey(
        'message.Message',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Последнее прочитанное сообщение')

    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чатов'
