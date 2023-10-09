from django.db import models

# Create your models here.

class URLStore(models.Model):
    originaluri = models.TextField(null=True, blank=True)
    shorturi = models.URLField(unique=True, null=True)
    createdAt = models.DateTimeField(auto_now=True, null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, null=True)
    expiryAt = models.DateField(null=True)

