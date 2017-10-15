# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User
class UserAdmin(admin.ModelAdmin):
        class Meta:
                model = User
admin.site.register(User,UserAdmin)

