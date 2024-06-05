
from django.urls import path
from .views import *
app_name='attendanceapp'    
    
    
urlpatterns=[
    path('record/', RecordAttendanceView.as_view(), name='record_attendance'),
    path('list/', AttendanceListView.as_view(), name='attendance_list'),
    path('update/<int:pk>/', UpdateAttendanceView.as_view(), name='update_attendance'),
    path('delete/<int:pk>/', DeleteAttendanceView.as_view(), name='delete_attendance'),
    
]