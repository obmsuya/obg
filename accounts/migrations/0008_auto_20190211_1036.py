# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-11 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190211_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downliner',
            old_name='userprofile',
            new_name='upliner',
        ),
    ]
