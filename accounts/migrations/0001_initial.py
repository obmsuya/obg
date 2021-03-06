# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 09:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upliner', models.CharField(default='', max_length=50)),
                ('downliner', models.IntegerField(default=0)),
                ('Maelezo', models.CharField(default='', max_length=100)),
                ('Proffession', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('region', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
