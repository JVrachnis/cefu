# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import messages, auth , sessions
from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect
import hashlib
import datetime
import time
from django.views.generic.edit import FormView
def start_session(request, user):
        request.session['user']=user.username
        request.session['user_id']=user.user_id
        return request
def chat(request):
        response = render(request,"index.html")
        if 'user_id' in request.session:
                #user_id = request.session['user_id']
                username = request.session['user']
                response = render(request,"chat.html",{'username':username})
                if (request.method == 'POST') and ('logout' in request.POST):
                        del request.session['user_id']
                        del request.session['user']
                        response = render(request,"index.html")
        return response
def get_login(request):
        if request.POST.get("email", "") !='':
                email =request.POST.get("email")
                password = hashlib.md5(request.POST.get('password').encode()).hexdigest()
                login(email,password,request)
def login(email , password,request):
        if User.objects.filter(email=email, password=password).exists():
                user = User.objects.get(email=email)
                start_session(request,user)
def singup(request):
        form = UserForm(request.POST or None)
        if form.is_valid():
                password = form.cleaned_data.get('password')
                repeatpassword = form.cleaned_data.get('repeatpassword')
                if password == repeatpassword:
                        save_it = User()
                        save_it.username = form.cleaned_data.get('username')
                        save_it.password = hashlib.md5(password.encode()).hexdigest()
                        save_it.birthday = form.cleaned_data.get('birthday')
                        save_it.email = form.cleaned_data.get('email')
                        save_it.save()
                        login(save_it.email ,save_it.password,request)

def home(request):
        if request.method == 'POST':
                if 'singup' in request.POST:
                        singup(request)
                elif 'login' in request.POST:
                        get_login(request)
        response = chat(request)
        return response
