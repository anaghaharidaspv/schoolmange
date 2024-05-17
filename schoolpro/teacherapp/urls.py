
from django.urls import path
from .views import *


urlpatterns=[
    path('teacherlogin',TeacherLogin.as_view(),name='teacher_login'),
    path('teacherprofile',TeacherProfile.as_view(),name='teacher_profile'),
    path('teacherlogout',TeacherLogout.as_view(),name='teacher_logout'),
    path('password_update/<int:id>',ChangePassword.as_view(),name='pass_reset'),
    path('loginotp',LoginEmailOtp.as_view(),name='loginotp'),
    path('verifyotp',OtpVerification.as_view(),name='verifyotp'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('files/', FileListView.as_view(), name='file_list'),
    path('delete/<int:pk>', DeleteFileView.as_view(), name='delete_file'),

]