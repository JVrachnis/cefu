# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singups', '0002_auto_20171004_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singup',
            old_name='nickname',
            new_name='username',
        ),
        migrations.AddField(
            model_name='singup',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='password'),
        ),
    ]
