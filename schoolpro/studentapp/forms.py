from django import forms
from adminapp.models import Student


class StudentLoginForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['username','password']


class CC(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('first_name','last_name','courses')