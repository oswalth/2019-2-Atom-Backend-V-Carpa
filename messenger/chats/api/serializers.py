from rest_framework import serializers
from chats.models import Chat


class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('title', 'is_group_chat', 'topic')

    def create(self, validated_data):
        chat = Chat.objects.create(host=self.context['request'].user,
                                 **validated_data)
        return chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class ChatPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('title', 'topic')