from django.db import models

class Translation(models.Model):
    language_code = models.CharField(max_length=5)
    text = models.TextField()
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
