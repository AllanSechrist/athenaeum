from itertools import chain
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import ReaderBookHistory, TextbookHistory
from students.models import Student
from courses.models import Course


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
        reader_history = ReaderBookHistory.objects.filter(course_id=course_id)
        textbook_history = TextbookHistory.objects.filter(course_id=course_id)
        history_list = list(chain(reader_history, textbook_history))
        return history_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs['student_id']
        course = get_object_or_404(Course, id=course_id)
        context['course'] = course
        return context


class HistoryByStudentListView(ListView):
    template_name = "relationships/history_by_student_list.html"
    context_object_name = "history_by_student_list"

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        reader_history = ReaderBookHistory.objects.filter(student_id=student_id)
        textbook_history = TextbookHistory.objects.filter(student_id=student_id)
        history_list = list(chain(reader_history, textbook_history))
        return history_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        context['student'] = student
        return context