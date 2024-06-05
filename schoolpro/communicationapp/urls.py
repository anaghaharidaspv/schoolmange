
from django.urls import path
from .views import *
urlpatterns = [
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement_create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement_update/<int:pk>/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcement_delete/<int:pk>', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('addnote/', AddNotifications.as_view(), name='add_notification'),
    path('note_list/', ViewNotificationsList.as_view(), name='view_notifications'),
    path('note_update/<int:id>/', UpdateNotification.as_view(), name='update_notifications'),
    path('note_delete/<int:id>/', DeleteNotification.as_view(), name='delete_notifications'),

]