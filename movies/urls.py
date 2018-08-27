from django.contrib import admin
from django.urls import path
from movies.views import homePage,addMovie,editMovie,deleteMovie
urlpatterns = [
    path('',homePage,name="movies"),
    path('addMovie',addMovie,name="addMovie"),
    path('<int:id>',editMovie,name="editMovie"),
    path('<int:id>/delete',deleteMovie,name="deleteMovie")
    
]
