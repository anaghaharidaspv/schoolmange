from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import TeacherAttendance
from .forms import AttendanceForm




class RecordAttendanceView(View):
    def get(self, request):
        form = AttendanceForm()
        return render(request, 'attendance/record_attendance.html', {'form': form})

    def post(self, request):
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendanceapp:attendance_list')
        return render(request, 'attendance/record_attendance.html', {'form': form})

class AttendanceListView(View):
    def get(self, request):
        attendances = TeacherAttendance.objects.all()
        return render(request, 'attendance/attendance_list.html', {'attendances': attendances})
    
class UpdateAttendanceView(View):
    def get(self, request, pk):
        attendance = TeacherAttendance.objects.get( pk=pk)
        form = AttendanceForm(instance=attendance)
        return render(request, 'attendance/update_attendance.html', {'form': form})

    def post(self, request, pk):
        attendance = TeacherAttendance.objects.get(pk=pk)
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendanceapp:attendance_list')
        return render(request, 'attendance/update_attendance.html', {'form': form})

class DeleteAttendanceView(View):
    def get(self, request, pk):
        attendance =TeacherAttendance.objects.get(pk=pk)
        attendance.delete()
        return redirect('attendanceapp:attendance_list')
