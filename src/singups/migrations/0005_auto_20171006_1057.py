# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singups', '0004_auto_20171005_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singup',
            old_name='first_name',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='singup',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='singup',
            name='username',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]