# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-11 07:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_userprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downliner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('january', models.IntegerField(default=0)),
                ('february', models.IntegerField(default=0)),
                ('march', models.IntegerField(default=0)),
                ('april', models.IntegerField(default=0)),
                ('may', models.IntegerField(default=0)),
                ('june', models.IntegerField(default=0)),
                ('july', models.IntegerField(default=0)),
                ('august', models.IntegerField(default=0)),
                ('september', models.IntegerField(default=0)),
                ('october', models.IntegerField(default=0)),
                ('november', models.IntegerField(default=0)),
                ('december', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Downliner',
            },
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='downliner',
            new_name='member',
        ),
        migrations.AddField(
            model_name='downliner',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
    ]
