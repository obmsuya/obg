# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-11 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_auto_20190211_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='downliner',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
