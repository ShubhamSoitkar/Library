from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.lib_admin_signup, name= 'lib_admin_signup'),
    path('login/',views.lib_admin_login, name= 'lib_admin_login'),
    path('logout/', views.logoutview, name= 'lib_admin_logout'),
]