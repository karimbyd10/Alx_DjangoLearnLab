from django.db import models


# ===========================================================
# Author Model
# ===========================================================
# Represents an author in the system.
#
# Fields:
# - name: Stores the author's name.
#
# Relationship:
# One Author can have many Books (one-to-many).
# ===========================================================

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ===========================================================
# Book Model
# ===========================================================
# Represents a book written by an Author.
#
# Fields:
# - title: Title of the book.
# - publication_year: Year the book was published.
# - author: ForeignKey linking to Author.
#
# Relationship:
# Each Book belongs to ONE Author.
# An Author can have MULTIPLE Books.
#
# related_name='books' allows reverse lookup:
# author.books.all()
# ===========================================================

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"