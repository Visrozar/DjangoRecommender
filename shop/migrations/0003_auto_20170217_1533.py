# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shops_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopsProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='shopsproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Products'),
        ),
        migrations.AddField(
            model_name='shopsproducts',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shops'),
        ),
        migrations.AddField(
            model_name='products',
            name='shops',
            field=models.ManyToManyField(through='shop.ShopsProducts', to='shop.Shops'),
        ),
    ]