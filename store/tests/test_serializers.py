from unittest import TestCase

from django.contrib.auth.models import User
from django.db.models import Count, Case, When

from store.models import Book, UserBookRelation
from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_func(self):
        book_1 = Book.objects.create(name='Test book 1', author='Author 1', price=35)
        book_2 = Book.objects.create(name='Test book 2', author='Author 3', price=55)

        books = Book.objects.all().annotate(annotated_likes=Count(Case(When(userbookrelation__like=True, then=1)))).order_by('id')
        data = BooksSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'author': 'Author 1',
                'price': '35.00',
                'annotated_likes': 2
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'author': 'Author 3',
                'price': '55.00',
                'annotated_likes': 1

            },
        ]
        self.assertEqual(expected_data, data)
