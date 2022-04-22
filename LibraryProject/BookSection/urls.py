from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('displaybooks/',views.get_book_data, name = 'display_book'),
    path('addbookdata/',views.add_book, name= 'add_book'),
    path('updatebook/<int:id>',views.update_book, name = 'update_book'),
    path('deletebook/<int:id>',views.delete_book, name='deletebookentry')
]