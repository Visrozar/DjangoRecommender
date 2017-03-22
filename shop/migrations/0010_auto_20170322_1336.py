# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20170322_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommends',
            name='item',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='recommends',
            name='recommend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Products'),
        ),
    ]