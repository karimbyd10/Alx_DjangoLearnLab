from django.db import models

class Author(models.Model):
    """
    Author model represents a writer.
    An author can be associated with multiple books,
    forming a one-to-many relationship.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.
    Each book is linked to a single author using
    a ForeignKey relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

