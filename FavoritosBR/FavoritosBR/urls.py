"""
URL configuration for FavoritosBR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from FavoritosBR import views
from django.contrib.auth.views import LogoutView
from FavoritosBR.views import custom_logout


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'), 
    path("baseFilmes/", include('baseFilmes.urls')),
    path("usuarios/", include('usuarios.urls')),
    path('logout/', custom_logout, name='logout'),
    path('usuarios/', include('usuarios.urls')),
]
