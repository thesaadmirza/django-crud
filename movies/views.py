from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import MoviesForm
from .models import Movies
# Create your views here.
def homePage(request):
    movies =  Movies.objects.all()
    paginator = Paginator(movies, 5) 
    page = request.GET.get('page')
    context = {
        'movies' : paginator.get_page(page)
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
    if request.user.is_authenticated and request.user.is_head:
      return redirect('addMovie')
    movie = Movies.objects.get(id=id)
    
    form = MoviesForm(request.POST or None , instance=movie)
    
    if form.is_valid():
        form.save()
        return redirect('/') 
    else:
        context = {
            'form' : MoviesForm(instance=movie),
            'id' : id
        }
    return render(request,"editMovie.html",context)

def deleteMovie(request,id):
    Movies.objects.filter(id=id).delete()
    return redirect('/')
      