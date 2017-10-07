
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.shortcuts import render
from .forms import SingUpForm
from .models import SingUp
from django.http import HttpResponseRedirect
import md5
import datetime
from django.views.generic.edit import FormView
def set_cookie(response, key, value, days_expire = 7):
  if days_expire is None:
    max_age = 365 * 24 * 60 * 60  #one year
  else:
    max_age = days_expire * 24 * 60 * 60 
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, max_age=max_age, expires=expires)

def home(request):
	if 'user' in request.COOKIES:
		nickname = request.COOKIES['user']
		response = render(request,"main.html",{'nickname':nickname})
		if request.method == 'POST':
			response = render(request,"singup.html",{'form':SingUpForm})
			response.delete_cookie("user")
		return response

	else:
		if request.method == 'POST':
			if 'singup' in request.POST:
				form = SingUpForm(request.POST or None)
				if form.is_valid():
					save_it = SingUp()
					save_it.username = form.cleaned_data.get('username')
					save_it.password = md5.new(form.cleaned_data.get('password')).hexdigest()
					save_it.nickname = form.cleaned_data.get('nickname')
					save_it.email = form.cleaned_data.get('email')
					save_it.save()
			elif 'login' in request.POST:
				if request.POST.get("username", "")!='':
					username = request.POST.get("username", "")
					password = md5.new(request.POST.get('password')).hexdigest()
					user = SingUp.objects.get(username=username)
					if user.password == password:
						#messages.success(request, 'Profile details updated.')
						response = render(request,"main.html",{'nickname':user.nickname})
						set_cookie(response,'user',user.nickname)
						return response
						#return HttpResponseRedirect('/main')
		return render(request,"singup.html",{'form':SingUpForm})
