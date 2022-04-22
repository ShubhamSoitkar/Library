from dataclasses import fields
from rest_framework import serializers
from BookSection.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'