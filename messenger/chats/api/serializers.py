from rest_framework import serializers
from chats.models import Chat
from user_profile .models import User, Member
from message.models import Message


class MemberPostSerializers(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Member()._meta.get_field('id'))
    class Meta:
        model = Member
        fields = ("id",)


class ChatPostSerializer(serializers.ModelSerializer):
    members = MemberPostSerializers('members', many=True)
    class Meta:
        model = Chat
        fields = ('title', 'is_group_chat', 'topic', 'members')


    def create(self, validated_data):
        members = (validated_data.get('members', None))
        if members:
            validated_data.pop('members')
            chat = Chat.objects.create(host=self.context['request'].user,
                                        **validated_data)
            for member in members:
                user = User.objects.filter(id=member['id'])
                if len(user) != 1:
                    continue
                Member.objects.create(
                    user=user[0],
                    chat=chat,
                )
        return chat



class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'last_read_message')


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    members = MemberSerializers('members', many=True)
    last_message = MessageSerializers('last_message')
    class Meta:
        model = Chat
        fields = '__all__'


class ChatPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('title', 'topic')