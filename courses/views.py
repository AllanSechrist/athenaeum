from django.views.generic import ListView, DetailView
from .models import Course
from books.models import StudentBookRelation, Book


class CourseListView(ListView):
    model = Course
    context_object_name = "course_list"
    template_name = "course/course_list.html"

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