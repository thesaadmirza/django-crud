from django import forms
from .models import Movies
class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            'title',
            'genre',
            'numberInStock',
            'dailyRentalRate'
        ]

