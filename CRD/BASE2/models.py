from django.db import models

# Create your models here.
# class MyFiles(models.Model):
#     name=models.CharField(max_length=50)
#     path=models.CharField(max_length=300)

class Stockage(models.Model):
    name=models.CharField(max_length=255)
    media_root=models.CharField(max_length=255)
    media_url=models.CharField(max_length=255)
    