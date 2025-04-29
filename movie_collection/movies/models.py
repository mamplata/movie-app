from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title