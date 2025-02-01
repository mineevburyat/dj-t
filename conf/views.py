from django.shortcuts import render
from django.views.debug import default_urlconf

def welcome(request):
    return default_urlconf(request)