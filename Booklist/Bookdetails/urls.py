from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('addbook/', views.book_form, name="book_insert"),             ## GET and POST for insertion
    path('<int:id>/', views.book_form, name="book_update"),       ## GET and POST for update 
    path('delete/<int:id>/', views.book_delete, name="book_delete"),
    path('', views.book_list, name="book_list"),                            ## GwET request to retrieve and display all books

    path('addgenre/', views.add_genre, name="add_genre"),
    path('genre/', views.genre_listy, name="genre_listy"),
    path('<int:id>/', views.add_genre, name="update_genre"),       ## GET and POST for update 
    # path('delete/<int:id>/', views.genre_delete, name="genre_delete"),
]
 