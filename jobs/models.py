from django.db import models
from devices.models import Device

class PlaybookJob(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    playbook_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
    output = models.TextField(blank=True)

    def __str__(self):
        return f"{self.playbook_name} on {self.device.hostname}"
