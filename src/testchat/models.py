from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.timezone import datetime
# Create your models here.
class Message(models.Model):
	
        message_id = models.AutoField(primary_key=True)
        user_id = models.models.IntegerField()
	nickname = models.CharField(max_length=120,null=True,blank=True)
        message = models.TextField()
        timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        def __unicode__(self):
                return smart_unicode(self.nickname)

