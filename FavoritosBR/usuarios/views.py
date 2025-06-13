from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def login(request):
    return render(request, "login.html")
