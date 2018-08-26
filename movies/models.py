from django.db import models
# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=60)
    genreId= models.IntegerField()
    numberInStock = models.IntegerField()
    dailyRentalRate = models.FloatField()
