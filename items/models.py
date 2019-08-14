from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

# serializer decode http data structure to python data structure


class Item (models.Model):
    name = models.CharField(max_length=15, default="")
    price = models.CharField(max_length=20, default="")
    year = models.CharField(max_length=20, default="")
    imgs = ArrayField(models.CharField(max_length=500), blank=True)
    favs = models.IntegerField(default=0)
