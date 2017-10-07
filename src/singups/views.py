
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.shortcuts import render
from .forms import SingUpForm
from .models import SingUp
from django.http import HttpResponseRedirect
import md5
from django.views.generic.edit import FormView
def home(request):
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
					messages.success(request, 'Profile details updated.')
					return render(request,"main.html",{'nickname':user.nickname})
					#return HttpResponseRedirect('/main')
	return render(request,"singup.html",{'form':SingUpForm})
