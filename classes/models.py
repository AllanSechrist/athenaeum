import uuid
from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    """Store the names of the teachers"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Class(models.Model):
    DAYS = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
    ]
    """
    Creates a class for the school year
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.course} - {self.day} - {self.teacher}"
    
    def get_absolute_url(self):
        pass
    