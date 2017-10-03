# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import SingUp
class SingUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SingUp
admin.site.register(SingUp,SingUpAdmin)
