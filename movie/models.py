from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    """Model for store all movies  genres."""

    title = models.CharField(max_length=100)


class Actor(models.Model):
    """Model for store any actor from movies."""

    name = models.CharField(max_length=100)


class Movie(models.Model):
    """Model for store movies with their base information in our service."""

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    similar_movies = models.ManyToManyField("Movie")
