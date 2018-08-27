from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import MoviesForm
from .models import Movies
# Create your views here.
def homePage(request):
    context = {
        'movies' : Movies.objects.all()
    }
    return render(request,"home.html",context)

def addMovie(request):
    form = MoviesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/') 
    else:
        context = {
            'form' : MoviesForm()
        }
    return render(request,"addMovie.html",context)

def editMovie(request,id):
    return render(request,"addMovie.html",context)

def deleteMovie(request,id):
    Movies.objects.filter(id=id).delete()
    return redirect('/')
      