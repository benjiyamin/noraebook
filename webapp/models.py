from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title