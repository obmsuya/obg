# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-05 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180105_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
