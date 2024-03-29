# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20171026_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='authentication.User'),
        ),
    ]
