from django.contrib import admin
from .models import Book, StudentBookRelation

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "level",)

admin.site.register(Book, BookAdmin)
admin.site.register(StudentBookRelation)

