from django.db import models


class ExamSubmission(models.Model):
    full_name = models.CharField(max_length=150)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.course}'