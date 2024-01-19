from django.urls import path
from . import views
from .templates import *

urlpatterns = [
    path('', views.landing),
    path('movies/', views.moviesHandler)
]
