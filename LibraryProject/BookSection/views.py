from django.shortcuts import render, redirect
from BookSection.forms import BookForm
from BookSection.models import Book



def get_book_data(request):
    bookobj = Book.objects.all()
    template_name = 'BookSection/displaybook.html'
    context = {'bookobj':bookobj}
    return render(request,template_name,context)


def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('display_book')
    return render(request, 'BookSection/addbook.html',{'form':form})

def update_book(request,id):
    bookobj = Book.objects.get(pk = id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=bookobj)
        if form.is_valid():
            form.save()
            return redirect('display_book')
    form = BookForm(instance=bookobj)
    return render(request,'BookSection/addbook.html',{'form':form})

def delete_book(request,id):
    bookobj = Book.objects.get(pk = id)
    if request.method == 'POST':
        bookobj.delete()
        return redirect('display_book')
    template_name = 'BookSection/confirmation.html'
    return render(request, template_name,{'bookobj':bookobj})