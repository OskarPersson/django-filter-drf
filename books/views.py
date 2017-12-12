# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django_filters import rest_framework as filters

from rest_framework import serializers, viewsets

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ( 'id', 'title', 'null_boolean', 'boolean',)


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['null_boolean', 'boolean']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filter_class = BookFilter
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = BookSerializer
