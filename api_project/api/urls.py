from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize DRF router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Keep your read-only ListAPIView if needed
    path('books/', BookList.as_view(), name='book-list'),

    # Include all router-generated URLs for full CRUD
    path('', include(router.urls)),
]

