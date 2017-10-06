# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.timezone import datetime
import md5
# Create your models here.
class SingUp(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=120,null=True,blank=True,unique=True)
	password = models.CharField(('password'), max_length=32,null=True,blank=True)
	nickname = models.CharField(max_length=120,null=True,blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.email)
	def set_password(raw_password,x):
		return md5.new(raw_password).hexdigest()
