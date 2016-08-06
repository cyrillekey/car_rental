# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-29 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20160623_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=system.models.uploaded_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('car_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('num_of_seats', models.IntegerField()),
                ('cost_par_day', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='movie_name',
            new_name='car_name',
        ),
    ]