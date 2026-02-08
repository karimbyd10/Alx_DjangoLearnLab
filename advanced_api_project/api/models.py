from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    This establishes the 'one' side of a one-to-many relationship
    between Author and Book.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a single book written by an author.
    Each book is linked to exactly one author using a ForeignKey,
    while an author can be linked to many books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables author.books access
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

