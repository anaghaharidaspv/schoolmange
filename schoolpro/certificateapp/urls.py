from django.urls import path
from .views import *



urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjectscreate', SubjectCreateView.as_view(), name='subject_create'),
    path('subjectsupdate/<int:pk>/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subjectsdelete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
     path('list/', ReportCardListViewall.as_view(), name='list'),
    path('cardlist/<int:id>', ReportCardListView.as_view(), name='reportcard_list'),
    path('reportcreate/', ReportCardCreateView.as_view(), name='reportcard_create'),
    path('reportupdate/<int:pk>/', ReportCardUpdateView.as_view(), name='reportcard_update'),
    path('reportdelete/<int:pk>/', ReportCardDeleteView.as_view(), name='reportcard_delete'),
    path('achievement/<int:pk>/', ReportCardView.as_view(), name='achievement_view'),
    
    
]
