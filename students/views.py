from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Student
from relationships.models import StudentBookRelation
from courses.models import Course


class StudentListView(ListView):
    model = Student
    context_object_name = "student_list"
    template_name = "students/student_list.html"

class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        student_relations = StudentBookRelation.objects.filter(student=student)
        context['student_relations'] = student_relations
        
        course_ids = set(relation.course_id for relation in student_relations)

        courses_with_student = Course.objects.filter(id__in=course_ids)
        context['courses_with_student'] = courses_with_student

        return context
