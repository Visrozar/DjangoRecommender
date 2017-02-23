from django.db import models

class Shops(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=400, default=0)
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=1000)
    shops = models.ManyToManyField(Shops, through='ShopsProducts', through_fields=('product', 'shop'),)

    def __str__(self):
        return self.name

class ShopsProducts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
