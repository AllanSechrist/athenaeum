from django.test import TestCase
from django.urls import reverse

from .models import Book, TextBook


class BookTests(TestCase):
    """
    Test for readers/library books
    """
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter",
            author = "JK Rowling",
            publisher = "Random House",
            level = "9",
            is_library_book = False,
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.publisher}", "Random House")
        self.assertEqual(f"{self.book.level}", "9")
        self.assertFalse(self.book.is_library_book)

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_detail.html")


class TextbookListViewTest(TestCase):
    """
    Tests for Textbook list view
    """
    def setUp(self):
        # Create some sample books
        TextBook.objects.create(
            title="Book 1",
            publisher="Publisher 1",
            grade_level="G3",
            isbn="1234567890",
        )
        TextBook.objects.create(
            title="Book 2",
            publisher="Publisher 2",
            grade_level="ADV",
            isbn="1234567890",
        )

    def test_textbook_list_view(self):
        url = reverse("textbook_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/textbook_list.html")
        self.assertQuerysetEqual(
            response.context["book_list"],
            ["<Book: Book 1>", "<Book: Book 2>"],
            ordered=False
        )


class TextbookDetailViewTest(TestCase):
    """
    Tests for textbook detail view
    """
    def setUp(self):
        # Create a sample book
        self.textbook = TextBook.objects.create(
            title="Sample Book",
            publisher="ABC Publishing",
            grade_level="G1",
            isbn="1234567890",
        )

    def test_book_detail_view(self):
        url = reverse("textbook_detail", args=[self.textbook.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/textbook_detail.html")
        self.assertEqual(response.context["textbook"], self.textbook)


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













