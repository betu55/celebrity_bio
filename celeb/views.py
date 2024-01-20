from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def landing(request):
#     return HttpResponse(f'<h1>This is the landig page</h1><h3>status_code: {HttpResponse.status_code}</h1>')

def landing(request):
    return render(request, 'dummyTemplate.html')


def moviesHandler(request):
    return HttpResponse(f'<h2>This is the movies handler page</ht>')
