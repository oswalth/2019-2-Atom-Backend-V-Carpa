from rest_framework import serializers
from message.models import Message
from attachment.models import Attachment
from chats.models import Chat
import magic


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Chat()._meta.get_field('id'))
    class Meta:
        model = Chat
        fields = ('id', )


class MessageSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Message()._meta.get_field('id'))
    class Meta:
        model = Message
        fields = ('id', )


class AttachmentPostSerializer(serializers.ModelSerializer):
    message = MessageSerializer('message', many=False)
    chat = ChatSerializer('chat', many=False)
    class Meta:
        model = Attachment
        fields = ('content', 'chat', 'message')

    
    def create(self, validated_data):
        content = validated_data['content']
        chat = Chat.objects.filter(id=validated_data['chat']["id"])[0]
        message = Message.objects.filter(id=validated_data['message']["id"])[0]
        validated_data.pop('content')
        attachment = Attachment(chat=chat, message=message)
        attachment.attachment_type = magic.from_buffer(content.read(), mime=True)
        attachment.content = content
        attachment.save()
        return attachment