from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
]
