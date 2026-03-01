from rest_framework import serializers
from .models import PlaybookJob

class PlaybookJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaybookJob
        fields = "__all__"