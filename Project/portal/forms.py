from django import forms

from .models import ExamSubmission


class ExamForm(forms.ModelForm):
    class Meta:
        model = ExamSubmission
        fields = ['full_name', 'course', 'year', 'address', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }