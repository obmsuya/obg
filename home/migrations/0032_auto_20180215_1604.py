# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-15 13:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20180212_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.RemoveField(
            model_name='item',
            name='width_field',
        ),
    ]
