from django.db import models
# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=60)
    genres= models.name = models.ForeignKeyField(Genres, on_delete=models.CASCADE)
    numberInStock = models.IntegerField()
    dailyRentalRate = models.FloatField()

class Genres(models.Model):
    name = CharField(max_length=60)