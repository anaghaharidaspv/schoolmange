import random
from django.conf import settings
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import *
from .forms import *
from attendanceapp.models import *
from django.utils.dateparse import parse_date


    
class indexview(View):
    def get(self,request):
        return render(request,'index.html')
       
    
 
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = adminmodel.objects.get(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            return redirect('dashboard')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class LogoutView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        logout(request)
        return redirect('login')


class AddCourseView(View):
    def get(self, request):
        return render(request, 'course/add_course.html')

    def post(self, request):
        name = request.POST.get('name')
        Course.objects.create(name=name)
        return redirect('course_list')


class UpdateCourseView(View): 
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        return render(request, 'course/update_course.html', {'course': course})

    def post(self, request, pk):
        course = Course.objects.get(pk=pk)
        name = request.POST.get('name')
        course.name = name
        course.save()
        return redirect('course_list')


class DeleteCourseView(View):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        return render(request, 'course/delete_course.html', {'course': course})

    def post(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return redirect('course_list')


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'course/course_list.html', {'courses': courses})


class AddBatchView(View):
    def get(self, request):
        return render(request, 'batch/add_batch.html')

    def post(self, request):
        name = request.POST.get('name')
        Batch.objects.create(name=name)
        return redirect('batch_list')


class UpdateBatchView(View):
    def get(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        return render(request, 'batch/update_batch.html', {'batch': batch})

    def post(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        name = request.POST.get('name')
        batch.name = name
        batch.save()
        return redirect('batch_list')


class DeleteBatchView(View):
    def get(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        return render(request, 'batch/delete_batch.html', {'batch': batch})

    def post(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        batch.delete()
        return redirect('batch_list')


class BatchListView(View):
    def get(self, request):
        batches = Batch.objects.all()
        return render(request, 'batch/batch_list.html', {'batches': batches})


class TeacherCreateView(View):
    def get(self,request):
        form=TeacherForm()
        return render(request,'teacher/teacher_create.html',{'form':form})
    def post(self,request):
        if request.method=='POST':

            form=TeacherForm(request.POST)
            if form.is_valid():
                name= form.cleaned_data['name']
                user_name=name.lower().replace('','') # Convert name to lowercase and remove spaces
                random_number=random.randint(1000,9999)
                password=f'{user_name}{random_number}'  # Create password by combining the username and random number
                teacher=form.save(commit=False) # Create a model instance without saving to the database yet
                teacher.username=user_name
                teacher.password=password
                form.save()   # Save the model instance to the database
                #send mail to teacher which contains username and password
                subject='Account Information'
                message=f'Hi {name}\n\n your Username i :{user_name} and Password is :{password}\n\n Please reset password after first login'
                send_mail_from=settings.EMAIL_HOST_USER
                recipient_list=[form.cleaned_data['email']]
                send_mail(subject,message,send_mail_from,recipient_list)
                return redirect('teacher_list')


class TeacherUpdateView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        form = TeacherForm(instance=teacher)
        return render(request, 'teacher/teacher_update.html', {'form': form})

    def post(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # Redirect to a URL name for the teacher list
        return render(request, 'teacher/teacher_update.html', {'form': form})


class TeacherDeleteView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        return render(request, 'teacher/teacher_delete.html', {'teacher': teacher})

    def post(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return redirect('teacher_list')  # Redirect to a URL name for the teacher list


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, 'teacher/teacher_list.html', {'teachers': teachers})


class StudentCreateView(View):
    def get(self,request):
        form=Studentform()
        return render(request,'student/student_create.html',{'form':form})
    def post(self,request):
        if request.method=='POST':

            form=Studentform(request.POST)
            if form.is_valid():
                name= form.cleaned_data['first_name']
                user_name=name.lower().replace('','') # Convert name to lowercase and remove spaces
                random_number=random.randint(1000,9999)
                password=f'{user_name}{random_number}'  # Create password by combining the username and random number
                student=form.save(commit=False) # Create a model instance without saving to the database yet
                student.username=user_name
                student.set_password(password)
                form.save()   # Save the model instance to the database
                #send mail to teacher which contains username and password
                subject='Account Information'
                message=f'Hi {name}\n\n your Username i :{user_name} and Password is :{password}\n\n Please reset password after first login'
                send_mail_from=settings.EMAIL_HOST_USER
                recipient_list=[form.cleaned_data['email']]
                send_mail(subject,message,send_mail_from,recipient_list)
                return redirect('student_list')


class StudentUpdateView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        form = Studentform(instance=student)
        return render(request, 'student/student_update.html', {'form': form})

    def post(self, request, pk):
        student = Student.objects.get(pk=pk)
        form = Studentform(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to a URL name for the teacher list
        return render(request, 'student/student_update.html', {'form': form})


class StudentDeleteView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        return render(request, 'student/student_delete.html', {'student':student })

    def post(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('student_list')  # Redirect to a URL name for the teacher list


class StudentListView(View):
    def get(self, request):
        student = Student.objects.all()
        return render(request, 'student/student_list.html', {'student': student})

class AttendanceReportView(View):
    def get(self, request):
        return render(request, 'Attendance/attendance_report.html')
    def post(self, request):
        start_date = parse_date(request.POST.get('start_date'))
        end_date = parse_date(request.POST.get('end_date'))
        teacher_id = request.POST.get('teacher_id')
        if start_date and end_date:
            if teacher_id:
                attendances = TeacherAttendance.objects.filter(date__range=[start_date, end_date], teacher_name_id=teacher_id)
            else:
                attendances = TeacherAttendance.objects.filter(date__range=[start_date, end_date])
        else:
            attendances = TeacherAttendance.objects.none()
        return render(request, 'Attendance/attendance_report.html', {
            'attendances': attendances,
            'start_date': start_date,
            'end_date': end_date,
            'teacher_id': teacher_id
        })
class LoadStates(View):
    def get(self,request,*args,**kwrags):
        countryid=request.GET.get('country_id')
        states=State1.objects.filter(country=countryid).all()
        print(states)
        return JsonResponse (list(states.values('id', 'state_name')), safe=False)
class LoadCity(View):
    def get(self,request,*args,**kwrags):
        stateid=request.GET.get('state_id')
        cities=City1.objects.filter(state=stateid).all()
        return JsonResponse(list(cities.values('id', 'city_name')), safe=False)