# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-23 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]