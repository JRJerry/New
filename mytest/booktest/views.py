from django.shortcuts import render

# Create your views here.

from django.http import *

def index(request)：
    return HttpResponse('hello')
