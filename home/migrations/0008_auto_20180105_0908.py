# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-05 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post2_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post2',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='post2',
            name='updated',
        ),
        migrations.AddField(
            model_name='post2',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post2',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
