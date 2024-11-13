import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "Author Name"  # Replace with the specific author's name
books_by_author = Author.objects.get(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# Query 2: List all books in a library
library_name = "Library Name"  # Replace with the library's name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:")
for book in books_in_library:
    print(book.title)

# Query 3: Retrieve the librarian for a library
library_name = "Library Name"  # Replace with the library's name
library = Library.objects.get(name=library_name)
librarian = library.librarian
print(f"The librarian for {library_name} is {librarian.name}.")
