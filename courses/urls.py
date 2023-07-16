from django.urls import path

from .views import CourseListView, CourseDetailView, CourseByDayListView

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("<str:day>/", CourseByDayListView.as_view(), name="courses_day"),
    path("<str:day>/<uuid:pk>/", CourseDetailView.as_view(), name="course_detail"),
]