from django.views.generic import ListView, DetailView
from .models import Student


class StudentListView(ListView):
    model = Student
    context_object_name = "student_list"
    template_name = "students/student_list.html"

class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "students/student_detail.html"
