from django import forms
from adminapp.models import Student
from django_recaptcha.fields import ReCaptchaField

class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha=ReCaptchaField()

class CC(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('first_name','last_name','courses')