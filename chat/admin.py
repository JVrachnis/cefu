# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Chat,Message
class ChatAdmin(admin.ModelAdmin):
        class Meta:
                model = Chat
admin.site.register(Chat,ChatAdmin)

class MessageAdmin(admin.ModelAdmin):
        class Meta:
                model = Message
admin.site.register(Message,MessageAdmin)
