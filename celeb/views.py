from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from .models import *
from .gpt import *

# Create your views here.


class CelebView(generics.ListAPIView):
    queryset = Celeb.objects.all()
    serializer_class = CelebSerializer


class MovieView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET'])
def search(request):
    if request.method == "GET":
        celeb_data = celebDetail(request.GET.get('key'))
        return Response(celeb_data)
    else:
        return Response({'error': 'Method not allowed'})
