from rest_framework import serializers
from .models import Book, Genrek

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genrek
        fields = "__all__"
