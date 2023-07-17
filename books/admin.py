from django.contrib import admin
from .models import Book, TextBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "level",)


@admin.register(TextBook)
class TextBookAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "grade_level", "isbn")

