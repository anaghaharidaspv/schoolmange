from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('studentlogin',StudentLogin.as_view(),name='student_login'),
    path('studentprofile',StudentProfile.as_view(),name='student_profile'),
    path('studentlogout',StudentLogout.as_view(),name='student_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]