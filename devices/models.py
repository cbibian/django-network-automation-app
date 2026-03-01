from django.db import models

class DeviceGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    hostname = models.CharField(max_length=100, unique=True)
    mgmt_ip = models.GenericIPAddressField()
    os_type = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    group = models.ForeignKey(DeviceGroup, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.hostname

