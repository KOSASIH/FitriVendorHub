from django.db import models

class Notification(models.Model):
    message = models.CharField(max_length=255)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
