from rest_framework import serializers
from .models import CMLSettings

class CMLSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMLSettings
        fields = "__all__"