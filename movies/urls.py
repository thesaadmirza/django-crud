from django.contrib import admin
from django.urls import path
from movies.views import homePage,addMovie
urlpatterns = [
    path('',homePage,name="Details"),
    path('addMovie',addMovie,name="addMovie"),
    path('<int:id>',viewMovie,name="viewMovie"),
    path('<int:id>/delete',deleteMovie,name="deleteMovie")
    
]
