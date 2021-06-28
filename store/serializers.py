from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Book, UserBookRelation


class BooksSerializer(ModelSerializer):
    annotated_likes = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author', 'annotated_likes')




class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
