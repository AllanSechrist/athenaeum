import uuid
from django.db import models
from django.urls import reverse

from students.models import Student


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    level = models.CharField(max_length=1)
    students = models.ManyToManyField(Student, through="StudentBookRelation")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    

class StudentBookRelation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} - {self.book}"

    