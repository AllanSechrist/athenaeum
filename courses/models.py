import uuid
from django.db import models


class Course(models.Model):
    """
    Used to create a course with all information
    related to the course.
    """
    COURSE_TYPES = [
        ("After School", "After School"),
        ("PreAfter", "PreAfter"),
        ("Graduate 1", "Graduate 1"),
        ("Graduate 2", "Graduate 2"),
        ("Graduate 3", "Graduate 3"),
        ("Advanced", "Advanced"),
        ("Baby", "Baby"),
        ("Kindergarten 2", "Kindergarten 2"),
        ("Kindergarten 1", "Kindergarten 1"),
        ("PreSchool 2", "PreSchool 2"),
        ("PreSchool 1", "PreSchool 1"),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,)
    type = models.CharField(max_length=5, choices=COURSE_TYPES)
  
    