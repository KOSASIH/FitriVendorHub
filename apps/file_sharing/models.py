from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files/')
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField('Vendor', related_name='shared_files')
