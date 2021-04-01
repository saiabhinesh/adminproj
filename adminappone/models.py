from django.db import models

# Create your models here.
class person(models.Model):
    pname=models.CharField(max_length=250)
    page=models.IntegerField()