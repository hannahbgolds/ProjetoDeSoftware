from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def filmes(request):
    return render(request,"filmes.html")

