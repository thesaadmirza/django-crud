from django.db import models
# Create your models here.
class Genres(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=60)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    numberInStock = models.IntegerField()
    dailyRentalRate = models.FloatField()
    def __str__(self):
        return self.title

