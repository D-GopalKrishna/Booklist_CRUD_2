from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


# Create your views here.

def book_list(request):
    context = {'book_kaster':Book.objects.all()}
    return render(request, "Bookdetails/book_list.html", context)

def book_form(request, id=0):
    if request.method == 'GET':      ## GET Request
        if id == 0:   #insert
            form = BookForm()  
        else:      #update
            bookin = Book.objects.get(pk=id)
            form = BookForm(instance=bookin)
        return render(request, "Bookdetails/book_form.html", {'form':form})  
    else:                            ## POST Request
        if id == 0:
            form = BookForm(request.POST)
        else:
            bookin = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=bookin)
        if form.is_valid():
            form.save()
        return redirect('/books/list')
    
def book_delete(request, id):
    bookin = Book.objects.get(pk=id)
    bookin.delete()
    return redirect('/books/list')