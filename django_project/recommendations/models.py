from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    name = models.CharField(max_length=200)
    genr = models.ManyToManyField(Genre)
    imdb_rateing = models.FloatField()
    release_date = models.DateField()
