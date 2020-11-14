from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.book_form, name="book_insert"),             ## GET and POST for insertion
    path('<int:id>/', views.book_form, name="book_update"),       ## GET and POST for update 
    path('delete/<int:id>/', views.book_delete, name="book_delete"),
    path('list/', views.book_list, name="book_list"),                            ## GwET request to retrieve and display all books
]
 