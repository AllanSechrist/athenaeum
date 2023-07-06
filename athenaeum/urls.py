from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # user management
    path("accounts/", include("allauth.urls")),
    # local
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
    path("students/", include("students.urls")),
    path("courses/", include("courses.urls")),
]
