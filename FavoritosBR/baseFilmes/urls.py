from django.urls import path
from . import views

urlpatterns = [
    path("", views.filmes_lista, name="filmes"),
    path("roleta/", views.filmes_roleta, name="filmes_roleta"),
]
