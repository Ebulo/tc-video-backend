from rest_framework import serializers
from streaming_backend.utils import getModel


class VideoReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = getModel("vdo_api.Video")
        fields = "__all__"


class VideoReadOnlyHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = getModel("vdo_api.Video")
        fields = "__all__"
