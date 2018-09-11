from django.db import models
# Create your models here.
class Genres(models.Model):
    name = models.CharField(max_length=60,blank=False)
    def __str__(self):
        return self.name
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)



class Movies(models.Model):
    title = models.CharField(max_length=60)
    genre = models.ForeignKey(Genres,related_name='genre', on_delete=models.CASCADE,blank=False)
    numberInStock = models.IntegerField()
    dailyRentalRate = models.FloatField()

    def __str__(self):
        return self.title   

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

