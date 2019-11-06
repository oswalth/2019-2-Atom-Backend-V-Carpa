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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    added_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{} at {}'.format(self.content, self.added_at)

    class Meta():
        ordering = ('-added_at',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    # sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    attachment_type = models.CharField(max_length=16, blank=False)
    url = models.CharField(max_length=128)

    def __str__(self):
        return '{} from {}'.format(self.attachment_type, self.url)
        
    class Meta():
        ordering = ('chat',)
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
