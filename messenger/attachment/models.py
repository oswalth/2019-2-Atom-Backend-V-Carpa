from django.db import models
from chats.models import Chat
from message.models import Message

def upload_router(instance, filename):
    if 'image' in instance.attachment_type:   
        return 'chat_{}/images/{}'.format(instance.chat.id, filename)
    elif 'audio' in instance.attachment_type:   
        return 'chat_{}/audios/{}'.format(instance.chat.id, filename)
    elif 'video' in instance.attachment_type:   
        return 'chat_{}/videos/{}'.format(instance.chat.id, filename)
    else:
        return 'chat_{}/documents/{}'.format(instance.chat.id, filename)


class Attachment(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Чат вложения')
    message = models.ForeignKey(
        Message,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Сообщение вложения')
    attachment_type = models.CharField(
        max_length=16, blank=False, verbose_name='Тип вложения')
    content = models.FileField(upload_to=upload_router, max_length=(10 * 1024 * 1024), null=True)
    
    url = models.CharField(max_length=128, verbose_name='Ссылка вложения')

    def __str__(self):
        return '{} from {}'.format(self.attachment_type, self.url)

    class Meta():
        ordering = ('chat',)
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'