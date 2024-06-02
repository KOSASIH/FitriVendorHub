from django.db import models

class VendorPerformance(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    task_completion_rate = models.DecimalField(max_digits=5, decimal_places=2)
    response_time = models.DecimalField(max_digits=5, decimal_places=2)
    quality_of_work = models.DecimalField(max_digits=5, decimal_places=2)
