from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing(request):
    return HttpResponse(f'<h1>This is the landig page</h1><h3>status_code: {HttpResponse.status_code}</h3>')