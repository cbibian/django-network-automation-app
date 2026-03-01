from django.db import models

class CMLSettings(models.Model):
    name = models.CharField(max_length=100, default="default", unique=True)
    base_url = models.URLField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    lab_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"CML Settings ({self.name})"