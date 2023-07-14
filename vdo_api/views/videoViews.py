from rest_framework import viewsets
from rest_framework import permissions
from vdo_api.serializers.videoSerializer import VideoReadOnlySerializer
from streaming_backend.utils import getModel

class VideoViewSet(viewsets.ModelViewSet):
    model = getModel("vdo_api.Video")
    queryset = model.objects.all().order_by('-created_at')
    serializer_class = VideoReadOnlySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
