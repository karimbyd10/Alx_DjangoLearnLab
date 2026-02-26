from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# ===========================================================
# BookSerializer
# ===========================================================
# Serializes all fields of the Book model.
#
# Includes custom validation:
# - publication_year must NOT be in the future.
# ===========================================================

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom field-level validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# ===========================================================
# AuthorSerializer
# ===========================================================
# Serializes Author model.
#
# Includes nested BookSerializer to dynamically include
# all books related to an author.
#
# Because Book model defines:
#   related_name='books'
#
# Django automatically creates reverse relation:
#   author.books.all()
#
# We use:
#   books = BookSerializer(many=True, read_only=True)
#
# many=True → because an author can have multiple books.
# read_only=True → prevents nested creation inside Author.
# ===========================================================

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']