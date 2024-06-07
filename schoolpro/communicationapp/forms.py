from dataclasses import fields
from django import forms
from .models import Announcement1, Notifications
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement1
        fields = ['title', 'message','expiry_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class NotificationsForm(forms.ModelForm):
    class Meta:
        model=Notifications
        fields='__all__'