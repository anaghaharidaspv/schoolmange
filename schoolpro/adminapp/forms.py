from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','email','phone_number','course','batch','batch','country','state','city']

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','email','phone_number','address','date_of_birth', 'gender','courses' ,'batch','country','state','city' ]