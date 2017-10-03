# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class SingUp(models.Model):
	first_name = models.CharField(max_length=120,null=True,blank=True)
	last_name = models.CharField(max_length=120,null=True,blank=True)
	email = models.CharField(max_length=120,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	def __inicode__(self):
		return smart_unicode(self.email)
