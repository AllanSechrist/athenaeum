from django.urls import path

from .views import BookListView, BookDetailView, TextBookListView, TextBookDetailView

urlpatterns = [
    path("readers/", BookListView.as_view(), name="book_list"),
    path("readers/<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("textbooks/", TextBookListView.as_view(), name="textbook_list"),
    path("textbooks/<uuid:pk>/", TextBookDetailView.as_view(), name="textbook_detail"),

]