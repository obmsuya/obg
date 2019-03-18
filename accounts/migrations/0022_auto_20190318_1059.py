# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0021_remove_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='backofice',
            new_name='Proffession',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='uplinerphone',
            new_name='account',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profilemake',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='downliner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Maelezo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='accountdescription',
            field=models.CharField(default='', max_length=200),
        ),
    ]
