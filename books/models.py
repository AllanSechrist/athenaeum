import uuid
import string
from django.db import models
from django.urls import reverse


def generate_level_choices():
    """
    Creates choices for leveled readers
    levels is made up of the numbers 1 ~ 9
    and the letters A ~ R
    """
    levels = [str(num) for num in range(1 ,10)] + list(string.ascii_uppercase)[:18]
    choices = [(level, level) for level in levels]
    return choices


class Book(models.Model):
    """
    Creates a book that is shared by students and
    read together in the Advance and Afterschool
    classes.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    level = models.CharField(max_length=1, choices=generate_level_choices())
    is_library_book = models.BooleanField(default=False)
    # students = models.ManyToManyField('students.Student', through="StudentBookRelation")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    

class TextBook(models.Model):
    GRADE_LEVELS = [
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
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=500)
    publisher = models.CharField(max_length=500)
    grade_level = models.CharField(max_length=5, choices=GRADE_LEVELS)
    isbn = models.CharField(max_length=13) # ISBN numbers have a length of 10 or 13
    # students = models.ManyToManyField('students.Student', through="StudentBookRelation")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("textbook_detail", args=[str(self.id)])
    

class StudentBookRelation(models.Model):
    """
    A model that connects students, books, and courses.
    Courses will have specific books that are connected
    to the students of that course.
    """
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    textbook = models.ForeignKey(TextBook, on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} - {self.book} - {self.textbook} - {self.course}"
    

class ReaderBookHistory(models.Model):
    """
    A model that keeps track of the readers a student
    has been assigned. 
    """
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    reader = models.ForeignKey(Book, on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.reader} - {self.start_date} - {self.finish_date}"
    

class TextbookHistory(models.Model):
    """
    A model that keeps track of the textbooks a student
    has been assigned. 
    """
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    textbook = models.ForeignKey(TextBook, on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.textbook} - {self.start_date} - {self.finish_date}"
    