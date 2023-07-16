from django.views.generic import ListView, DetailView
from .models import Book, TextBook


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"

class TextBookListView(ListView):
    model = TextBook
    context_object_name = "textbook_list"
    template_name = "books/textbook_list.html"

class TextBookDetailView(DetailView):
    model = TextBook
    context_object_name = "textbook"
    template_name = "books/textbook_detail.html"
