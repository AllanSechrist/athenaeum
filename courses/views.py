from typing import Any
from django.db import models
from django.db.models import Case, When, F
from django.views.generic import ListView, DetailView
from .models import Course
from books.models import StudentBookRelation, Book


class CourseListView(ListView):
    model = Course
    context_object_name = "course_list"
    template_name = "course/course_list.html"

    def get_queryset(self):
        ordering = Case(
            When(day="M", then=0),
            When(day="T", then=1),
            When(day="W", then=2),
            When(day="Th", then=3),
            When(day="F", then=4),
            default=5,
            output_field=models.IntegerField()
        )
        return Course.objects.order_by(ordering, F('teacher__name'))
    
class CourseByDayListView(ListView):
    model = Course
    context_object_name = "course_list"
    template_name = 'course/course_day_list.html'

    def get_queryset(self):
        day = self.kwargs['day']
        return Course.objects.filter(day=day)

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "course/course_detail.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        student_book_relations = StudentBookRelation.objects.filter(course=course).select_related('student')
        students = [relation.student for relation in student_book_relations]
        books = Book.objects.filter(studentbookrelation__in=student_book_relations)
        context['students'] = students
        context['books'] = books
        return context