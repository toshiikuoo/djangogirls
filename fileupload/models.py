from django.db import models
from django.utils import timezone

class FileModel(models.Model):
    title = models.CharField(max_length=100)
    uploadplace = models.FileField(upload_to='upload/')
    uploaded_date = models.DateTimeField(default=timezone.now)
