from django import forms
from .models import Subject, Professor, Student
from django.contrib.auth.models import User
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Professor.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Professor.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name']



