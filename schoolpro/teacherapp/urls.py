
from django.urls import path
from .views import *
app_name='teacherapp'


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
    path('import/',ImportDataView.as_view(),name='import'),
    path('export/',ExportToExcelView.as_view(),name='exportdata'),
    path('achievement', AchievementListView.as_view(), name='achievement-list'),
    path('achievementcreate/', AchievementCreateView.as_view(), name='achievement-create'),
    path('achievementupdate/<int:pk>/', Editachievement.as_view(), name='achievement-update'),
    path('deleteachievement/<int:pk>',Deleteachievement.as_view(),name='achievement-delete'),
]
