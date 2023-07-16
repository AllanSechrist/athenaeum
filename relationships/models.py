from django.db import models


class StudentBookRelation(models.Model):
    """
    A model that connects students, books, and courses.
    Courses will have specific books that are connected
    to the students of that course.
    """
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    textbook = models.ForeignKey("books.Textbook", on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} - {self.book} - {self.textbook} - {self.course}"
    

class ReaderBookHistory(models.Model):
    """
    A model that keeps track of the readers a student
    has been assigned. 
    """
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    reader = models.ForeignKey("books.Book", on_delete=models.CASCADE)
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
    textbook = models.ForeignKey("books.TextBook", on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.textbook} - {self.start_date} - {self.finish_date}"
    