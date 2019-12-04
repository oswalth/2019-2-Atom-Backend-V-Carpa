from message.models import Message
from .serializers import MessageSerializer, MessagePostSerializer
from rest_framework import viewsets


class MessageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


    def get_serializer_class(self):
        if self.action == 'create':
            return MessagePostSerializer
        else:
            return MessageSerializer