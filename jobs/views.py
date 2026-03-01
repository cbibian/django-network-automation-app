from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PlaybookJob
from .serializers import PlaybookJobSerializer
from .ansible_runner import run_playbook

class PlaybookJobViewSet(viewsets.ModelViewSet):
    queryset = PlaybookJob.objects.all()
    serializer_class = PlaybookJobSerializer

    @action(detail=True, methods=["post"])
    def run(self, request, pk=None):
        job = self.get_object()
        run_playbook(job.id)
        job.refresh_from_db()
        return Response(PlaybookJobSerializer(job).data)
