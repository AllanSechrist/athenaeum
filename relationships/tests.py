from django.test import TestCase, Client
from django.urls import reverse
from .models import ReaderBookHistory, TextbookHistory


class ReaderBookHistoryListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some reader book history objects for testing
        self.history1 = ReaderBookHistory.objects.create(
            student_id=1,
            reader_id=1,
            course_id=1,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = ReaderBookHistory.objects.create(
            student_id=1,
            reader_id=2,
            course_id=2,
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
        

class TextbookHistoryListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some textbook history objects for testing
        self.history1 = TextbookHistory.objects.create(
            student_id=1,
            textbook_id=1,
            course_id=1,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = TextbookHistory.objects.create(
            student_id=1,
            textbook_id=2,
            course_id=2,
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


class HistoryByCourseListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some reader book history objects for testing
        self.history1 = ReaderBookHistory.objects.create(
            student_id=1,
            reader_id=1,
            course_id=1,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = ReaderBookHistory.objects.create(
            student_id=2,
            reader_id=2,
            course_id=1,
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


class HistoryByStudentListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.history1 = ReaderBookHistory.objects.create(
            student_id=1,
            reader_id=1,
            course_id=1,
            start_date='2023-01-01',
            finish_date='2023-01-31'
        )
        self.history2 = ReaderBookHistory.objects.create(
            student_id=1,
            reader_id=2,
            course_id=2,
            start_date='2023-02-01',
            finish_date='2023-02-28'
        )
    
    def test_history_by_student_list_view(self):
        student_id = 1 
        url = reverse('history_by_student_list', args=[student_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationships/history_by_student_list.html')
        self.assertContains(response, self.history1.reader.title)
        self.assertContains(response, self.history2.reader.title)
