from unittest import TestCase
from store.models import Book
from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_func(self):
        book_1 = Book.objects.create(name='Test book 1', author='Author 1', price=35)
        book_2 = Book.objects.create(name='Test book 2', author='Author 3', price=55)

        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'author': 'Author 1',
                'price': '35.00'

            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'author': 'Author 3',
                'price': '55.00'
            },
        ]
        self.assertEqual(expected_data, data)
