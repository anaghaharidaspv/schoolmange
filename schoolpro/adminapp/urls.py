
from django.urls import path
from .views import *

urlpatterns = [
    path('',indexview.as_view(),name='index'),
    path('adminlogin', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('add_course/', AddCourseView.as_view(), name='add_course'),
    path('update_course/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
    path('delete_course/<int:pk>',DeleteCourseView.as_view() , name='delete_course'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('add_batch/', AddBatchView.as_view(), name='add_batch'),
    path('update_batch/<int:pk>', UpdateBatchView.as_view(), name='update_batch'),
    path('delete_batch/<int:pk>', DeleteBatchView.as_view(), name='delete_batch'),
    path('batches', BatchListView.as_view(), name='batch_list'),

    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('update_teacher/<int:pk>/', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>/', TeacherDeleteView.as_view(), name='delete_teacher'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('liststates',LoadStates.as_view(),name='list_states'),
    path('listcities',LoadCity.as_view(),name='list_cities'),
    
    path('create_student/', StudentCreateView.as_view(), name='create_student'),
    path('update_student/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete_student/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('attendancereport',AttendanceReportView.as_view(), name='attendance_report')

]






