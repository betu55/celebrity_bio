from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
