from attachment.models import Attachment
from .serializers import AttachmentSerializer, AttachmentPostSerializer
from rest_framework import viewsets


class AttachmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AttachmentSerializer
    queryset = Attachment.objects.all()


    def get_serializer_class(self):
        if self.action == 'create':
            return AttachmentPostSerializer
        else:
            return AttachmentSerializer