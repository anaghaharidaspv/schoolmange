from dataclasses import fields
from django import forms
from .models import Announcement, Notifications
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
        }
class NotificationsForm(forms.ModelForm):
    class Meta:
        model=Notifications
        fields='__all__'