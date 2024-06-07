
from django.urls import path
from .views import *
urlpatterns = [
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('announcementdashboard',AnnouncementsDahboardListView.as_view(),name='announcement_dashboard'),
    path('addnote/', AddNotifications.as_view(), name='add_notification'),
    path('note_list/', ViewNotificationsList.as_view(), name='view_notifications'),
    path('note_update/<int:id>/', UpdateNotification.as_view(), name='update_notifications'),
    path('note_delete/<int:id>/', DeleteNotification.as_view(), name='delete_notifications'),

]