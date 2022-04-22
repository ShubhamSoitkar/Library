from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        labels = {
            'book_name':'Book Name',
            'author_name': 'Author Name'
        }