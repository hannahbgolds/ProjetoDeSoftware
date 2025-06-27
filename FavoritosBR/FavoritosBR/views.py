from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request,"home.html")

def custom_logout(request):
    logout(request)
    return redirect('home')
