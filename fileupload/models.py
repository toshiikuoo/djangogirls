from django.db import models

class FileModel(models.Model):
    title = models.CharField(max_length=100)
    uploadplace = models.FileField(upload_to='upload/')
