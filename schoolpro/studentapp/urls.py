from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name='studentapp'


urlpatterns=[
    path('studentlogin',StudentLogin.as_view(),name='student_login'),
    path('studentprofile',StudentProfile.as_view(),name='student_profile'),
    path('studentlogout',StudentLogout.as_view(),name='student_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('studentslist/', StudentListView.as_view(), name='studentlist'),
    path('generate_certificate/<int:student_id>/', GenerateCertificateView.as_view(), name='generate_certificate'),
    path('view_message/<int:id>/', ViewNotificationMessage.as_view(), name='view_message'),
]
