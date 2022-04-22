from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'author_name']

admin.site.register(Book, BookAdmin)
