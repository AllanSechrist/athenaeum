from django.contrib import admin
from .models import ReaderBookHistory, TextbookHistory, StudentBookRelation


@admin.register(ReaderBookHistory)
class ReaderBookHistoryAdmin(admin.ModelAdmin):
    list_display = ("student", "reader", "course", "start_date", "finish_date")

@admin.register(TextbookHistory)
class TextbookHistoryAdmin(admin.ModelAdmin):
    list_display = ("student", "textbook", "course", "start_date", "finish_date")

@admin.register(StudentBookRelation)
class StudentBookRelation(admin.ModelAdmin):
    list_display = ("student", "book", "textbook", "course")
