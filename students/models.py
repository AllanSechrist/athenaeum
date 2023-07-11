import uuid
from django.db import models
from django.urls import reverse


class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    grade = models.CharField(max_length=25)
    full_name = f"{first_name} {last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])
    

