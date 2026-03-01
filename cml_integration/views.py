from rest_framework import viewsets
from .models import CMLSettings
from .serializers import CMLSettingsSerializer

class CMLSettingsViewSet(viewsets.ModelViewSet):
    queryset = CMLSettings.objects.all()
    serializer_class = CMLSettingsSerializer

