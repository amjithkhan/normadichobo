from distutils.command.upload import upload
from unicodedata import name
from django.db import models


class Destinations(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="pix")
    desc=models.TextField()
    cost=models.IntegerField()
    date=models.DateField(auto_now_add=True)

