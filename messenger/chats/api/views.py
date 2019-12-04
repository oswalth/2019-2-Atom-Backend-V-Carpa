from chats.models import Chat
from .serializers import ChatSerializer, ChatPostSerializer, ChatPutSerializer, MessageSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from user_profile.models import User, Member
from message.models import Message


# class ChatViewSet(viewsets.ModelViewSet):
#     """
#     #A viewset for viewing and editing user instances.
#     """
#     serializer_class = ChatPostSerializer
#     queryset = Chat.objects.all()
    
#     @action(detail=True, methods=['get'])
#     def read_message(self, request, pk):
#         user = User.objects.get(id=request.user.id)
#         print(user)
#         return Response({'status': pk})


from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()



class ChatDetailView(RetrieveAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    @staticmethod
    def read_message(user, chat):
        member = Member.objects.get(user=user, chat=chat)
        member.last_read_message = chat.last_message
        member.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if not request.user.is_anonymous:
            ChatDetailView.read_message(user=request.user, chat=instance)
        custom_response = dict(serializer.data)
        custom_response['messages'] = [MessageSerializers(msg).data for msg in Message.objects.filter(chat=instance)]
        return Response(custom_response)


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatPostSerializer
    


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatPutSerializer


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


