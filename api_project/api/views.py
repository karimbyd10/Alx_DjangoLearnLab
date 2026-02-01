from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API endpoint that allows all books to be viewed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView (optional to keep)
class BookList(generics.ListAPIView):
    """
    API endpoint to list all books (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD actions for Book model:
    - list: GET /books_all/
    - retrieve: GET /books_all/<id>/
    - create: POST /books_all/
    - update: PUT /books_all/<id>/
    - partial_update: PATCH /books_all/<id>/
    - destroy: DELETE /books_all/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Require user to be authenticated
    permission_classes = [permissions.IsAuthenticated]

    # Optional: admin-only permissions
    # permission_classes = [permissions.IsAdminUser]

