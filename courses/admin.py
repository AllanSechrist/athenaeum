from django.contrib import admin
from .models import Course, Teacher, StudentCourseRelation


class CourseAdmin(admin.ModelAdmin):
    list_display = ("type", "day", "teacher")


admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher)
admin.site.register(StudentCourseRelation)
