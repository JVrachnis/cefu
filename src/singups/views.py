# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def foo(request):
 return HttpResponse("Hello World!")
# Create your views here.
