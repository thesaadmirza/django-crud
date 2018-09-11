from movies.models import Movies,Genres
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Genres
        fields = ('id','name')


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Movies
        fields = ('title','genre','numberInStock','dailyRentalRate')

