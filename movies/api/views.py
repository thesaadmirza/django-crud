from rest_framework import generics
from movies.models import Movies
from rest_framework import viewsets
from movies.api.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieCreateAPIView(generics.CreateAPIView):
    permission_classes         = []
    authentication_classes     = []
    queryset                   = Movies.objects.all()
    serializer_class           = MovieSerializer

class MovieUpdateAPIView(generics.UpdateAPIView):
    permission_classes         = []
    authentication_classes     = []
    queryset                   = Movies.objects.all()
    serializer_class           = MovieSerializer

class MovieDeleteAPIView(generics.DestroyAPIView):
    permission_classes         = []
    authentication_classes     = []
    queryset                   = Movies.objects.all()
    serializer_class           = MovieSerializer