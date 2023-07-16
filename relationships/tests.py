from django.test import TestCase
from django.urls import reverse
from .models import TextbookHistory, ReaderBookHistory, StudentBookRelation
from students.models import Student
from books.models import Book, TextBook
from courses.models import Course


class ReaderListViewTest(TestCase):
    def setUp(self):
        # Create some sample books
        Book.objects.create(
            title="Book 1",
            author="Author 1",
            publisher="Publisher 1",
            level="A",
            is_library_book=False
        )
        Book.objects.create(
            title="Book 2",
            author="Author 2",
            publisher="Publisher 2",
            level="B",
            is_library_book=True
        )


    def test_book_list_view(self):
        url = reverse("book_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertQuerysetEqual(
            response.context["book_list"],
            ["<Book: Book 1>", "<Book: Book 2>"],
            ordered=False
        )

