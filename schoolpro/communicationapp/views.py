from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from pytz import timezone
from .models import Announcement1,Notifications
from .forms import AnnouncementForm,NotificationsForm

class AnnouncementListView(View):
    def get(self, request):
        announcements = Announcement1.objects.all()
        return render(request, 'announcements/announcements.html', {'announcements': announcements})
class AnnouncementCreateView(View):
    def get(self, request):
        form = AnnouncementForm()
        return render(request, 'announcements/create_announcement.html', {'form': form})
    def post(self, request):
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
        return render(request, 'announcements/create_announcement.html', {'form': form})
class AnnouncementDetailView(View):
    def get(self, request, pk):
        announcement = Announcement1.objects.get(pk=pk)
        return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})
class AnnouncementUpdateView(View):
    def get(self, request, pk):
        announcement = Announcement1.objects.get(pk=pk)
        form = AnnouncementForm(instance=announcement)
        return render(request, 'announcements/update_announcement.html', {'form': form, 'announcement': announcement})
    def post(self, request, pk):
        announcement = Announcement1.objects.get(pk=pk)
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
        return render(request, 'announcements/update_announcement.html', {'form': form, 'announcement': announcement})
class AnnouncementDeleteView(View):
    def get(self, request, pk):
        announcement = Announcement1.objects.get(pk=pk)
        announcement.delete()
        return redirect('announcement_list')
class AnnouncementsDahboardListView(View):
    def get(self, request):
        today=timezone.now().date()
        announcements = Announcement1.objects.filter(expiry_date__gte=today)
        return render(request, 'dashboard_announcement.html', {'announcements': announcements})
class AddNotifications(View):
    def get(self,request):
        form=NotificationsForm()
        return render(request,'notifications/add_notifications.html',{'form':form})
    def post(self,request):
        if request.method=='POST':
            form=NotificationsForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('view_notifications')
            else:
                return HttpResponse('validation failed')
class ViewNotificationsList(View):
    def get(self,request):
        notifications=Notifications.objects.all()
        return render(request,'notifications/list_notifications.html',{'notifications':notifications})
class UpdateNotification(View):
    def get(self,request,id):
        notification=Notifications.objects.get(id=id)
        form=NotificationsForm(instance=notification)
        return render(request,'notifications/update_notifications.html',{'form':form})
    def post(self,request,id):
        notification=Notifications.objects.get(id=id)
        if request.method=='POST':
            form=NotificationsForm(request.POST,request.FILES,instance=notification)
            if form.is_valid():
                form.save()
                return redirect('view_notifications')
            else:
                return HttpResponse('validation failed')
class DeleteNotification(View):
    def get(self,request,id):
        notification=Notifications.objects.get(id=id)
        notification.delete()
        return redirect('view_notifications')