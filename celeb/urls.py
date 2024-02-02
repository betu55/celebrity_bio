from django.urls import path
from . import views
from .templates import *

urlpatterns = [
    path('celebs/', views.CelebView.as_view()),
    path('movies/', views.MovieView.as_view()),
    path('search/', views.search)
]
