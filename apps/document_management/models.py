from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
