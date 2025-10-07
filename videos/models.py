from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

def current_year():
    return datetime.date.today().year

class Video(models.Model):
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-Fi"),
        ("Horror", "Horror"),
        ("Documentary", "Documentary"),
        ("Animation", "Animation"),
        ("Other", "Other"),
    ]

    movie_id = models.CharField("MovieID", max_length=20, primary_key=True)
    title = models.CharField("MovieTitle", max_length=200)
    actor1 = models.CharField("Actor1Name", max_length=100)
    actor2 = models.CharField("Actor2Name", max_length=100, blank=True)
    director = models.CharField("DirectorName", max_length=100)
    genre = models.CharField("MovieGenre", max_length=20, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(
        "ReleaseYear",
        validators=[MinValueValidator(1888), MaxValueValidator(current_year)]
    )

    created_at = models.DateTimeField(auto_now_add=True)  # optional helper
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.release_year})"
