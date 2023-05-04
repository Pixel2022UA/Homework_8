from django.db import models
from teachers.models import Teacher
from students.models import Student


class Group(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True
    )
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.group_name}"


class StudentsGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class LogMiddlewareModel(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    execution_time = models.DecimalField(max_digits=50, decimal_places=50)
