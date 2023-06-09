from django.contrib import admin
from .models import Book, StudentBookRelation


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "level",)


admin.site.register(StudentBookRelation)

