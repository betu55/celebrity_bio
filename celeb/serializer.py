from rest_framework import serializers
from .models import *


class CelebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celeb
        fields = ('id', 'name', 'age')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_year', 'celeb')
