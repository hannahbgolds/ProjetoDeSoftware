from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-vindo à página de baseFilmes!")
