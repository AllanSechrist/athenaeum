from django.test import TestCase, Client
from django.urls import reverse
from .models import ReaderBookHistory, TextbookHistory
from students.models import Student
from books.models import Book, TextBook
from courses.models import Course, Teacher


class BaseRelationshipsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_students()
        self.create_courses()
        self.create_readers()
        self.create_textbooks()

    def create_students(self):
        self.student1 = Student.objects.create(
            first_name = "Link",
            last_name = "Hyrule",
            grade = "G3",
        )
        self.student2 = Student.objects.create(
            first_name = "Zelda",
            last_name = "Hyrule",
            grade = "G2",
        )

    def create_courses(self):
        self.teacher = Teacher.objects.create(
            name = "Buzz"
        )
        self.course1 = Course.objects.create(
            type = "AC",
            day = "M",
            teacher = self.teacher,
            start_date = '2022-01-01',
            finish_date = '2022-12-10',
        )
        self.course2 = Course.objects.create(
            type = "ADV",
            day = "M",
            teacher = self.teacher,
            start_date = '2022-01-03',
            finish_date = '2022-12-13',
        )

    def create_readers(self):
        self.reader1 = Book.objects.create(
            title = "Harry Potter",
            author = "JK Rowling",
            publisher = "Random House",
            level = "Q",
            is_library_book = True
        )
        self.reader2 = Book.objects.create(
            title = "Magic Tree House",
            author = "Mary Pope Osborne",
            publisher = "Random House",
            level = "8",
            is_library_book = False
        )

    def create_textbooks(self):
        self.textbook1 = TextBook.objects.create(
            title = "New Wave Spelling A",
            publisher = "Pearson",
            grade_level = "AC",
            isbn = "1234567890",
        )
        self.textbook2 = TextBook.objects.create(
            title = "First ABCs",
            publisher = "Pearson",
            grade_level = "B",
            isbn = "0987654321",
        )

    


class ReaderBookHistoryListViewTest(BaseRelationshipsTest):
    def setUp(self):
        super().setUp()
        self.create_reader_book_history()

    def create_reader_book_history(self):
        # Create some reader book history objects for testing
        self.history1 = ReaderBookHistory.objects.create(
            student_id=self.student1.id,
            reader_id=self.reader1.id,
            course_id=self.course1.id,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = ReaderBookHistory.objects.create(
            student_id=self.student1.id,
            reader_id=self.reader2.id,
            course_id=self.course2.id,
            start_date='2023-02-01',
            finish_date='2023-02-28'
        )
    
    def test_reader_book_history_list_view(self):
        url = reverse('reader_history_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationships/reader_history_list.html')
        self.assertContains(response, self.history1.reader.title)
        self.assertContains(response, self.history2.reader.title)
        

class TextbookHistoryListViewTest(BaseRelationshipsTest):
    def setUp(self):
        super().setUp()
        self.create_textbook_history()

    def create_textbook_history(self):
        # Create some textbook history objects for testing
        self.history1 = TextbookHistory.objects.create(
            student_id=self.student1.id,
            textbook_id=self.textbook1.id,
            course_id=self.course1.id,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = TextbookHistory.objects.create(
            student_id=self.student1.id,
            textbook_id=self.textbook2.id,
            course_id=self.course2.id,
            start_date='2023-02-01',
            finish_date='2023-02-28'
        )

    
    def test_textbook_history_list_view(self):
        url = reverse('textbook_history_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationships/textbook_history_list.html')
        self.assertContains(response, self.history1.textbook.title)
        self.assertContains(response, self.history2.textbook.title)
        # Add more assertions as needed


class HistoryByCourseListViewTest(BaseRelationshipsTest):
    def setUp(self):
        super().setUp()
        self.create_reader_book_history()

    def create_reader_book_history(self):
        # Create some reader book history objects for testing
        self.history1 = ReaderBookHistory.objects.create(
            student_id=self.student1.id,
            reader_id=self.reader1.id,
            course_id=self.course1.id,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = ReaderBookHistory.objects.create(
            student_id=self.student2.id,
            reader_id=self.reader2.id,
            course_id=self.course1.id,
            start_date='2023-02-01',
            finish_date='2023-02-28'
        )
    
    def test_history_by_course_list_view(self):
        course_id = 1  
        url = reverse('history_by_course_list', args=[course_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationships/history_by_course_list.html')
        self.assertContains(response, self.history1.reader.title)
        self.assertContains(response, self.history2.reader.title)
        # Add more assertions as needed


class HistoryByStudentListViewTest(BaseRelationshipsTest):
    def setUp(self):
        super().setUp()
        self.create_reader_book_history()

    def create_reader_book_history(self):
        self.history1 = ReaderBookHistory.objects.create(
            student_id=self.student1.id,
            reader_id=self.reader1.id,
            course_id=self.course1.id,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = ReaderBookHistory.objects.create(
            student_id=self.student1.id,
            reader_id=self.reader2.id,
            course_id=self.course2.id,
            start_date='2023-02-01',
            finish_date='2023-02-28'
        )
    
    def test_history_by_student_list_view(self):
        student_id = self.student1.id 
        url = reverse('history_by_student_list', args=[student_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationships/history_by_student_list.html')
        self.assertContains(response, self.history1.reader.title)
        self.assertContains(response, self.history2.reader.title)
