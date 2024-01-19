from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Celebrity(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=20, null=True, blank=True)
    actors = models.ManyToManyField(Celebrity, related_name='movies')

    def __str__(self):
        return self.title
