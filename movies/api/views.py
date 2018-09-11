from rest_framework import generics,mixins
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

class MovieDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes         = []
    authentication_classes     = []
    queryset                   = Movies.objects.all()
    serializer_class           = MovieSerializer
    def put(self,request,*args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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