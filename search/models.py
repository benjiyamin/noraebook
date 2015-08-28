from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    favorites = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.user.username
