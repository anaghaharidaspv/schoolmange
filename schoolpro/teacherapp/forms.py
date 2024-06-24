from django import forms
from adminapp.models import Teacher
from .models import *


class TeacherLoginForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['username','password']

class OtpLoginForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['email']
        


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'



class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['student', 'score']
        
class Excelform(forms.Form):
    file=forms.FileField()
  




