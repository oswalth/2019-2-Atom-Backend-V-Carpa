from rest_framework import serializers
from message.models import Message
from user_profile.models import Member
from chats.models import Chat
from rest_framework.authtoken.models import Token


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Chat()._meta.get_field('id'))
    class Meta:
        model = Chat
        fields = ('id', )


class MessagePostSerializer(serializers.ModelSerializer):
    # chat = serializers.PrimaryKeyRelatedField(read_only=True)
    chat = ChatSerializer('chat', many=False)
    class Meta:
        model = Message
        fields = ('content', 'chat')

    
    def create(self, validated_data):
        token = self.context['request'].META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=token).user
        print("*"*100)
        print(user)
        print("*"*100)
        chat_id = validated_data['chat']["id"]
        chat = Chat.objects.filter(id=chat_id)[0]
        print(chat)
        message = Message.objects.create(sender=user,
                                        chat=chat,
                                        content=validated_data['content'])
       
        member = Member.objects.filter(user=user, chat=chat)[0]
        member.last_read_message = message
        member.save()
        chat.last_message = message
        chat.save()
        return message