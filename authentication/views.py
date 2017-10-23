# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import sessions
from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.shortcuts import redirect
import hashlib
import datetime
import time
from django.views.generic.edit import FormView
from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth import login,get_user
from django.contrib.auth.backends import ModelBackend
from django.core.mail import EmailMessage

def authenticate(email=None, password=None, **kwargs):
        UserModel = User()
        try:
                user = User.objects.get(email=email)
        except User.DoesNotExist:
                return None
        else:
                print("user does exixst and pass %s" % user.check_password(password))
                if user.check_password(password):
                        print(user.email_confirmed)
                        if user.email_confirmed == False:
                                user.email_confirm()
                                return None
                        elif user.is_active:
                                return user
        return None
def login(request,user,stay_login):
        request.session['user'] = user.id
        if stay_login:
                request.session.set_expiry(None)
        else:
                request.session.set_expiry(0)
        return chat(request)
def logout(request):
        del request.session['user']
        return request
def chat(request):
        username = User.objects.get(id = request.session['user'])
        response = render(request,"chat.html",{'username':username})
        if (request.method == 'POST') and ('logout' in request.POST):
                logout(request)
                response = redirect_to_chat(request)
        return response
def redirect_to_chat(request):
        response = render(request,"index.html")
        if 'user' in request.session:
                if request.session.get_expire_at_browser_close():
                        request = logout(request)
                        return render(request,"index.html")
                else:
                        return chat(request)
        return response
def get_login(request):
        if request.POST.get("email", "") !='':
                email =request.POST.get("email")
                password = request.POST.get('password')
                stay_login = request.POST.get('remember_me',"") == 'on'
                user = authenticate(email=email, password=password)
                print("%s %s %s %s" % (user.username,user.email,user.password,stay_login))
                return login(request,user,stay_login)
def singup(request):
        form = UserForm(request.POST or None)
        if form.is_valid():
                password = form.cleaned_data.get('password')
                repeatpassword = form.cleaned_data.get('repeatpassword')
                username= form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                birthday = form.cleaned_data.get('birthday')
                if password == repeatpassword:
                        save_it = User(email=email,username=username,birthday=birthday)
                        save_it.set_password(password)
                        save_it.save()
                        user = authenticate(email=email, password=password)
                        return login(request ,user)

def home(request):
        response = redirect_to_chat(request)
        if request.method == 'POST':
                if 'singup' in request.POST:
                        response = singup(request)
                elif 'login' in request.POST:
                        response = get_login(request)
        return response
def email_confirm(request,email,confirmation):
        try:
                user = User.objects.get(email=email)
        except ObjectDoesNotExist:
                print("didnt find smthing")
                return redirect('/')
        else:
                if confirmation == user.confirmation_code:
                        user.email_confirmed = True
                        user.save()
        return redirect('/')
