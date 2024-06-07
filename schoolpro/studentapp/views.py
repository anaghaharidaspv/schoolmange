from datetime import date
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CC
from adminapp.models import Student,Teacher
from communicationapp.models import Notifications
from django.template.loader import render_to_string
from django.db.models import Q
from .forms import StudentLoginForm


        
class StudentLogin(View):
    def get(self,request):
        form=StudentLoginForm()
        return render(request,'studentapp/student_login.html',{'form':form})
    def post(self,request):
        if request.method=='POST':
            form=StudentLoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                print(username,password)
                student=authenticate(request,username=username,password=password)
                print(student)
                if student is not None:
                    login(request,student)
                    return redirect('studentapp:student_profile')
                else:
                    msg='Wrong credentials'
                    return render(request,'studentapp/student_login.html',{'form':form,'msg':msg})
            return HttpResponse('validation failed')








    

class StudentProfile(View):
    def get(self,request):
        student=request.user
        print(student.id)
        #********************to see notifications in profile page********************
        stud_ent=Student.objects.get(username=student.username, email=student.email)
        s_course=stud_ent.courses
        print(s_course)
        s_batch=stud_ent.batch
        print(s_batch)
        teacher=Teacher.objects.get(course=s_course,batch=s_batch)
        notifications=Notifications.objects.filter(Q(teacher=teacher)| Q(teacher__isnull=True))  # to get queryset
        # with specific teacher id and without teacher id
        #**********end here*****************
        #******************to set reminders in profile*************
        reminders = []
        for notif in notifications:
            days = int((notif.expiry_date - date.today()).days)
            if 0 <= days <= 5:
                reminders.append((notif, days))
                print(reminders)
        return render(request,'studentapp/student_profile.html',{'student':student,'notifications':notifications,'reminders':reminders,'days':days})
        # return render(request,'student_profile.html',{'student':student,'notifications':notifications})
class StudentLogout(View):
    def get(self, request):
        logout(request)
        return redirect('studentapp:student_login')


from django.views.generic import ListView, View
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from adminapp.models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student/studentlist.html'
    context_object_name = 'students'

class GenerateCertificateView(View):
    def get(self, request,student_id):
        student = Student.objects.get(id=student_id)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{student.first_name}_{student.last_name}_certificate.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        p.setFont("Helvetica", 12)
        
        # Draw the certificate content
        
        p.drawCentredString(width / 2.0, height - 100, "Certificate of Completion")
        p.setFont("Helvetica", 18)
        p.drawCentredString(width / 2.0, height - 150, f"This is to certify that")
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2.0, height - 200, f"{student.first_name} {student.last_name}")
        p.setFont("Helvetica", 18)
        p.drawCentredString(width / 2.0, height - 250, f"has successfully completed the course")
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2.0, height - 300, f"{student.courses.name}")
        p.setFont("Helvetica", 16)
        p.drawCentredString(width / 2.0, height - 450, "Congratulations!")
        # Add a border (optional)
        p.rect(30, 30, width - 60, height - 60)
        
        # Save the PDF file
        
        p.showPage()
        p.save()

        return response
    
class ViewNotificationMessage(View):
     def get(self,request,id):
        notification=Notifications.objects.get(id=id)
        return render(request,'notifications/notification_message.html',{'notification':notification})