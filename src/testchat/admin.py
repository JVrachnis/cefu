# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import SingUp
class MessageAdmin(admin.ModelAdmin):
        class Meta:
                model = Message
admin.site.register(Message,MessageAdmin)


