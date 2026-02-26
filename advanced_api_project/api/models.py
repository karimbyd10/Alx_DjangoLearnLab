from django.db import models

# -----------------------------------------------------------
# Author Model
# -----------------------------------------------------------
# Represents a book author.
# An author can have multiple books (one-to-many relationship).
# -----------------------------------------------------------

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# -----------------------------------------------------------
# Book Model
# -----------------------------------------------------------
# Represents a book written by an author.
# Each book belongs to one author.
# The 'author' field creates a ForeignKey relationship,
# establishing a one-to-many relationship:
#
# One Author → Many Books
#
# related_name="books" allows us to access all books of an
# author using: author.books.all()
# -----------------------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"