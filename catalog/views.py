from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import Language, Genre, Author, Book, BookInstance

# Create your views here.
def index(request):
    template = 'catalog/index.html'
    return render(request, template)

class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    # queryset = Genre.book_set.all()
    template = 'catalog/genre_detail.html'

"""class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template = 'catalog/author_list.html'
"""

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    # queryset = Author.book_set.objects.all()
    template = 'catalog/author_detail.html'

class BookDetailView(DetailView):
    model = Book
    # queryset = Book.books.objects.all()
    context_object_name = 'book'
    template = 'catalog/book_detail.html'