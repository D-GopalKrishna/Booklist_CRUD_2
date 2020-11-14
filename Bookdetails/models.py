from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Genrek(models.Model):
    nik = models.CharField(max_length=500)

    def __str__(self):
        return self.nik

class Book(models.Model):
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    ratings = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    genre = models.ForeignKey(Genrek, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    

