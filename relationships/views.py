from django.views.generic import ListView
from .models import ReaderBookHistory, TextbookHistory


class ReaderBookHistoryListView(ListView):
    model = ReaderBookHistory
    context_object_name = "reader_book_history_list"
    template_name = "relationships/reader_history_list.html"


class TextbookHistoryListView(ListView):
    model = TextbookHistory
    context_object_name = "textbook_history_list"
    template_name = "relationships/textbook_history_list.html"


class HistoryByCourseListView(ListView):
    template_name = "relationships/history_by_course_list.html"
    context_object_name = "history_by_course_list"

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        history_list = ReaderBookHistory.objects.filter(course_id=course_id) | TextbookHistory.objects.filter(course_id=course_id)
        return history_list


class HistoryByStudentListView(ListView):
    template_name = "relationships/history_by_student_list.html"
    context_object_name = "history_by_student_list"

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        history_list = ReaderBookHistory.objects.filter(student_id=student_id) | TextbookHistory.objects.filter(student_id=student_id)
        return history_list
