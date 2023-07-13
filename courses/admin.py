from django.contrib import admin
from .models import Course, Teacher


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("type", "day", "teacher")


admin.site.register(Teacher)
