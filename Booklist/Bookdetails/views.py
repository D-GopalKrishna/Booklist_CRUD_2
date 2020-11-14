from django.shortcuts import render, redirect
from .forms import BookForm, GenrekForm
from .models import Book, Genrek


# Create your views here.

def book_list(request):
    context = {'book_kaster':Book.objects.all()}
    return render(request, "Bookdetails/book_list.html", context)

def book_form(request, id=0):        ## By default id=0
    if request.method == 'GET':      ## GET Request
        if id == 0:   #insert
            form = BookForm()  
        else:      #update
            bookin = Book.objects.get(pk=id)
            form = BookForm(instance=bookin)
        return render(request, "Bookdetails/book_form.html", {'form':form})  
    else:                            ## POST Request
        if id == 0:                  ## insert
            form = BookForm(request.POST)
        else:                       ## post
            bookin = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=bookin)
        if form.is_valid():
            form.save()
        return redirect('/')
    
def book_delete(request, id):
    bookin = Book.objects.get(pk=id)
    bookin.delete()
    return redirect('/')





## Add Genre

def genre_listy(request):
    # context = {'genre_kaster':Genrek.objects.get(pk=1)}
    return render(request, "Bookdetails/genre_list.html",)

def add_genre(request, id=0):
    if request.method == 'GET':  
        if id == 0:   # insert
            form2 = GenrekForm()
        else:   # Update
            genrein = Genrek.objects.get(pk=id)
            form2 = GenrekForm(instance=genrein)
        return render(request, 'Bookdetails/genre_form.html', {'form2' : form2})
    else:
        if id == 0:
            form2 = GenrekForm(request.POST)
        else:
            genrein = Genrek.objects.get(pk=id)
            form2 = GenrekForm(request.POST, instance=genrein)
        if form2.is_valid():
            form2.save()
        return redirect('/genre/')

    
# def genre_delete(request, id):
#     bookin = Genrek.objects.get(pk=id)
#     bookin.delete()
#     return redirect('/genre/')
  

