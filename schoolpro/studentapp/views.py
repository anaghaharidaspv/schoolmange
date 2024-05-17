from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login,logout,authenticate
from adminapp.views import LogoutView
from studentapp.forms import StudentLoginForm
from adminapp.models import Student

class StudentLogin(View):
    def get(self, request):
        return render(request, 'studentapp/student_login.html')

    def post(self, request):
        msg = ''
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request, user)
                return render(request,'studentapp/student_profile.html',{'user':user})
                msg = 'error'
            return render(request, 'studentapp/student_login.html',{ 'msg': msg})
    

class StudentProfile(View):
    def get(self, request):
        return render(request, 'studentapp/student_profile.html')

class StudentLogout(View):
    def get(self, request):
        logout(request)
        return redirect('student_login')

