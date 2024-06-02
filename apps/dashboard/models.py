from django.db import models

class DashboardWidget(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
