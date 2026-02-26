from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from datetime import datetime



# Provides CRUD operations for Author
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Provides CRUD operations for Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ===========================================================
# BookListView
# ===========================================================
# GET /books/
#
# Returns a list of all books.
# Publicly accessible (read-only).
# ===========================================================

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ===========================================================
# BookDetailView
# ===========================================================
# GET /books/<pk>/
#
# Retrieves a single book by ID.
# Publicly accessible (read-only).
# ===========================================================

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ===========================================================
# BookCreateView
# ===========================================================
# POST /books/create/
#
# Creates a new book.
# Only authenticated users allowed.
# ===========================================================

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Extra safeguard validation (optional override example)
    def perform_create(self, serializer):
        year = serializer.validated_data.get("publication_year")
        current_year = datetime.now().year

        if year > current_year:
            raise ValidationError("Publication year cannot be in the future.")

        serializer.save()


# ===========================================================
# BookUpdateView
# ===========================================================
# PUT/PATCH /books/<pk>/update/
#
# Updates an existing book.
# Only authenticated users allowed.
# ===========================================================

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ===========================================================
# BookDeleteView
# ===========================================================
# DELETE /books/<pk>/delete/
#
# Deletes a book instance.
# Only authenticated users allowed.
# ===========================================================

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]