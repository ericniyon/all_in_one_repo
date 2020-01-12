from django.db import models
from django.urls import reverse
# Create your models here.
STATUS =(
    (0, "Not Published"),
    (1, "Published")
)
class Album(models.Model):
    title       =       models.CharField(max_length=100)
    
    artist      =       models.CharField(max_length=200)
    status      =       models.IntegerField(choices=STATUS, default=0)


    def get_absolute_url(self):
        return reverse('album')
    def __str__(self):
        return self.title


class Song(models.Model):
    name            =       models.CharField(max_length=200)
    song_type       =       models.CharField(max_length=100)
    song_formt      =       models.CharField(max_length=20)
    album           =       models.ForeignKey(Album, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('album')
    def __str__(self):
        return self.name