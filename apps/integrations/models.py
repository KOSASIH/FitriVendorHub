from django.db import models

class Integration(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    tool = models.CharField(max_length=255)  # e.g. Asana, Trello, Jira
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
