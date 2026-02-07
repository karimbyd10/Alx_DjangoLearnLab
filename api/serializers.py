from rest_framework import serializers
from datetime import date
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer is responsible for converting Book model
    instances into JSON and validating incoming data.

    It serializes all fields of the Book model and includes
    custom validation to ensure the publication year is valid.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation method to ensure that the
        publication_year is not set in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer handles serialization of Author instances.

    It includes a nested BookSerializer to dynamically
    represent all books related to an author using
    Django's reverse relationship.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

