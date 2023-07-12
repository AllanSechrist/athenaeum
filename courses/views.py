from django.views.generic import ListView, DetailView
from .models import Course


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
        students = course.studentcourserelation_set.all()
        context['students'] = students
        return context