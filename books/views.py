from django.views.generic import ListView, DetailView
from .models import Book, TextBook, ReaderBookHistory, TextbookHistory


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

class ReaderBookHistoryListView(ListView):
    model = ReaderBookHistory
    context_object_name = "readerbookhistory"
    template_name = "books/reader_history_list.html"

class TextbookHistoryListView(ListView):
    model = TextbookHistory
    context_object_name = "textbookhistory"
    template_name = "books/textbook_history_list.html"

