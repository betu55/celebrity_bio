from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Celebrity(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=50)
    release_year = models.IntegerField(null=True, blank=True)
    celeb = models.ForeignKey(
        Celebrity, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')

    def __str__(self):
        return self.title


class Question(models.Model):

    question = models.CharField(max_length=300, null=True)
    answer = models.CharField(max_length=1,  null=True)

    def __str__(self):
        return self.question


class Option(models.Model):

    question = models.ForeignKey(
        Question, null=True, on_delete=models.CASCADE, related_name='options')
    letter = models.CharField(max_length=1, null=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
