from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
