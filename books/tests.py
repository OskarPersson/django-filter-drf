# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from django_filters import rest_framework as filters

from rest_framework.test import APIClient

from books.models import Book
from books.views import BookFilter

# Create your tests here.

class FilterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('book-list')

    def test_filterset(self):
        field = Book._meta.get_field('boolean')
        result = BookFilter.filter_for_field(field, 'boolean')
        self.assertIsInstance(result, filters.BooleanFilter)

    def test_filter_uppercase(self):
        book1 = Book.objects.create(title="foo", boolean=False, null_boolean=False)
        book2 = Book.objects.create(title="bar", boolean=True, null_boolean=True)
        res = self.client.get(self.url, data={'boolean': 'False'})
        self.assertEqual(len(res.data), 1)

    def test_filter_lowercase(self):
        book1 = Book.objects.create(title="foo", boolean=False, null_boolean=False)
        book2 = Book.objects.create(title="bar", boolean=True, null_boolean=True)
        res = self.client.get(self.url, data={'boolean': 'false'})
        self.assertEqual(len(res.data), 1)
