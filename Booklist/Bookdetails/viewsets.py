from rest_framework import viewsets
from . import models
from . import serializers

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    
class GenreViewsets(viewsets.ModelViewSet):
    queryset = models.Genrek.objects.all()
    serializer_class = serializers.GenreSerializer