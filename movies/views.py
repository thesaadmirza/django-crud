from django.shortcuts import render
from django.http import HttpResponse
from .forms import MoviesForm
from .models import Movies
# Create your views here.
def homePage(request):
    context = {
        'movie' : Movies.objects.get(id=1)
    }
    return render(request,"home.html",context)

def addMovie(request):
    form = MoviesForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : MoviesForm()
    }
    return render(request,"addMovie.html",context)
