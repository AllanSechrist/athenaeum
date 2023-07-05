import uuid
from django.db import models
from django.urls import reverse



class Teacher(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    COURSE_TYPES = [
        ("AC", "After School"),
        ("PA", "Pre-After"),
        ("G1", "Graduate 1"),
        ("G2", "Graduate 2"),
        ("G3", "Graduate 3"),
        ("ADV", "Advanced"),
        ("B", "Baby"),
        ("K2", "Kindergarten 2"),
        ("K1", "Kindergarten 1"),
        ("P2", "PreSchool 2"),
        ("P1", "PreSchool 1"),
    ]
    teachers = [(teacher.name, teacher.name) for teacher in Teacher.objects.all()]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    type = models.CharField(max_length=5, choices=COURSE_TYPES)
    teacher = None
    start_date = None
    end_date = None



