# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='birth_date',
            field=models.CharField(default='0000-00-00', max_length=10),
        ),
        migrations.AddField(
            model_name='page',
            name='death_data',
            field=models.CharField(default='0000-00-00', max_length=10),
        ),
    ]
