from django.shortcuts import render
from BookSection.models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser, IsAuthenticated


class BookInfo(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes =[TokenAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly]
