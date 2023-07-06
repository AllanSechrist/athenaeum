import uuid
from django.db import models
from django.urls import reverse



class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    DAYS = [
        ("M", "Monday"),
        ("T", "Tuesday"),
        ("W", "Wednesday"),
        ("Th", "Thursday"),
        ("F", "Friday"),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    type = models.CharField(max_length=5, choices=COURSE_TYPES)
    day = models.CharField(max_length=2, choices=DAYS)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # start_date = None
    # end_date = None

    def __str__(self):
        return f"{self.type} {self.day}"
    
    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])



