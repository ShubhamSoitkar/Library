import email
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import LibraryAdminForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
from .backends import CaseInsensitiveModelBackend

def lib_admin_signup(request):
    form = LibraryAdminForm()
    if request.method == 'POST':
        form = LibraryAdminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            form.save()
            return redirect('lib_admin_login')
    return render(request, 'LibraryAdmin/signup.html',{'form':form})



def lib_admin_login(request):
    if request.method == 'POST':
        em = request.POST.get('em')
        ps = request.POST.get('ps')
        user =CaseInsensitiveModelBackend().authenticate(request,username=em,password=ps)
        #user = authenticate(request,username=em,password=ps)
        user.backend='django.contrib.auth.backends.ModelBackend' #To again search in default auth of backend just like a normal username
        if user is not None:
            print('********',user.is_authenticated)
            login(request, user)
            return redirect('display_book')
    return render(request,'LibraryAdmin/login.html')

def logoutview(request):
    logout(request)
    return redirect('lib_admin_login')



