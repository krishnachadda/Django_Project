from django.contrib import admin

from .models import ExamSubmission


@admin.register(ExamSubmission)
class ExamSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'course', 'year', 'phone_number', 'created_at')
    search_fields = ('full_name', 'course', 'year', 'phone_number')