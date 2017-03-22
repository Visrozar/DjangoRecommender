from django.db import models

class Shops(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

class Products(models.Model):
    name = models.CharField(max_length=600)

class Recommends(models.Model):
    item = models.FloatField(default=0)
    recommend = models.ForeignKey(Products)
    value = models.FloatField(default=0)
