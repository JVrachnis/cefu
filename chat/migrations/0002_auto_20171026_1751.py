# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='chat_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='chat_type',
            new_name='type',
        ),
    ]