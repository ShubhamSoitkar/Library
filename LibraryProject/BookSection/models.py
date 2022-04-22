from django.db import models

class Book(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length= 150)
    author_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.book_id} {self.book_name} {self.author_name}'
        