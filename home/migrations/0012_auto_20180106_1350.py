# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-06 10:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180106_1341'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post3',
            new_name='category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
