# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-12 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20190212_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='secondgenb',
            field=models.IntegerField(default=0),
        ),
    ]
