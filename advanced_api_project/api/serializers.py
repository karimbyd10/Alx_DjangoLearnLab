from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# -----------------------------------------------------------
# BookSerializer
# -----------------------------------------------------------
# Serializes all fields of the Book model.
#
# Includes custom validation to ensure that
# publication_year is NOT set in the future.
# -----------------------------------------------------------

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


# -----------------------------------------------------------
# AuthorSerializer
# -----------------------------------------------------------
# Serializes the Author model.
#
# Includes nested serialization of related books using:
# books = BookSerializer(many=True, read_only=True)
#
# Because we set related_name="books" in the Book model,
# Django automatically creates a reverse relation:
#
# author.books.all()
#
# This allows dynamic nested serialization of all books
# related to an author.
# -----------------------------------------------------------

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']