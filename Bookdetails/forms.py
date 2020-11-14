from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('bookname', 'author', 'publisher', 'ratings', 'genre', 'description')
        labels = {
            'bookname' : 'Book Name',
            'author' : 'Author',
            'publisher' : 'Publisher',
            'ratings' : 'Ratings',
            'genre' : 'Genre',
            'description' : 'About',
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['genre'].empty_label = '  --------------- Select --------------    '