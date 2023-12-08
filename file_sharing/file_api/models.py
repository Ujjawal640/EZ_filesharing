from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=60)

class File(models.Model):
    filename = models.CharField(max_length=255)
    filetype = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
