from chats.models import Chat
from .serializers import ChatSerializer, ChatPostSerializer, ChatPutSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from user_profile.models import User


# class ChatViewSet(viewsets.ModelViewSet):
#     """
#     #A viewset for viewing and editing user instances.
#     """
#     serializer_class = ChatSerializer

    
#     @action(detail=True, methods=['get'])
#     def read_message(self, request, pk):
#         user = User.objects.get(id=request.user.id)
#         print(user)
#         return Response({'status': pk})

#     def get_queryset(self):
#         """
#         # This view should return a list of all the purchases
#         # for the currently authenticated user.
#         """
#         user = self.request.user
#         return Chat.objects.all()


from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatPostSerializer


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatPutSerializer


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


