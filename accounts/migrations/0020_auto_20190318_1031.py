# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20190212_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Proffession',
            new_name='backofice',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profilemake',
            field=models.CharField(default='', max_length=100),
        ),
    ]
