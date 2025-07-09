from django.urls import path, include
from . import views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('meus-filmes/', views.meus_filmes, name='meus_filmes'),
    path('marcar-assistido/', views.marcar_como_assistido, name='marcar_como_assistido'),
]
