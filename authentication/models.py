# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
# from django.utils.encoding import smart_unicode
from django.utils.timezone import datetime
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
import hashlib
import socket
# Create your models here.
class User(AbstractBaseUser):
        username = models.CharField(max_length=120,null=True,blank=True,unique=True)
        email = models.EmailField(unique=True)
        birthday = models.DateField(default=datetime.now,blank=True)
        date_joind = models.DateTimeField(auto_now=False, auto_now_add=True)
        date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        is_active = models.BooleanField(default=True)
        avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
        email_confirmed = models.BooleanField(default=False)
        confirmation_code = models.CharField(max_length=60,default=get_random_string(length=60))
        REQUIRED_FIELDS = ['username','birthday','email']
        USERNAME_FIELD = 'username'
        class Meta:
                verbose_name = _('user')
                verbose_name_plural = _('users')
        def email_confirm(user, **kwargs):
                '''
                Sends an email to this User.
                '''
                print("sending message to : %s" %user.email)
                server_ip = "127.0.0.1:8000" #socket.gethostbyname(request.META['SERVER_NAME'])
                link = "http://%s/emailconfirm/%s/%s" %(server_ip,user.email,user.confirmation_code)
                message ='hello %s , thanks for joining us<br>please confirm your email <a href="%s">here</a>' %(user.username,link)
                email = EmailMessage('Cefu email comfirmation', message, to=[user.email])
                email.content_subtype = "html"
                email.send()
                #send_mail("Cefu email confirmation", message, from_email, [user.email], **kwargs)
