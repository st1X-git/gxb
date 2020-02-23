from django.db import models

# Create your models here.

class Popular(models.Model):
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()


class Rated(models.Model):
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()


class ShopAll(models.Model):
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
