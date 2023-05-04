from datetime import date
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birthday = models.DateField(default=date.today)
    subject = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, birthday: {self.date_of_birthday}, subject: {self.subject}"
