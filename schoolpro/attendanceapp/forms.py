from .models import *
from django import forms



class AttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['date', 'teacher_name', 'arrival_time' , 'break_start_time', 'break_end_time','departure_time']