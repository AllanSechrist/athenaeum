from django.urls import path

from .views import ReaderBookHistoryListView, TextbookHistoryListView, HistoryByCourseListView, HistoryByStudentListView

urlpatterns = [
    path("/readers_history", ReaderBookHistoryListView.as_view(), name="reader_history_list"),
    path("/textbook_history", TextbookHistoryListView.as_view(), name="textbook_history_list"),
    path("courses/<int:course_id>/", HistoryByCourseListView.as_view(), name="history_by_course_list"),
    path("students/<int:student_id>/", HistoryByStudentListView.as_view(), name="history_by_student_list"),
]