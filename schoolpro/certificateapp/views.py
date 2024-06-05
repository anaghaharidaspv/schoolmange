from django.shortcuts import render
from .forms import SubjectForm,ReportcardForm
# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class SubjectListView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(request, 'certificateapp/sub_list.html', {'subjects': subjects})


class SubjectCreateView(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, 'certificateapp/subject_form.html', {'form': form})

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        return render(request, 'certificateapp/subject_form.html', {'form': form})

class SubjectUpdateView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        form = SubjectForm(instance=subject)
        return render(request, 'certificateapp/subject_update.html', {'form': form})

    def post(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        

class SubjectDeleteView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return redirect('subject_list')
    
    
 
class ReportCardListViewall(View):
    def get(self, request):
        reportcards = Reportcard.objects.all()
        return render(request, 'reportcard/report_list.html', {'reportcards': reportcards})
   
    


class ReportCardListView(View):
    def get(self, request,id):
        reportcards = Reportcard.objects.filter(stuname=id)
        return render(request, 'reportcard/report_listall.html', {'reportcards': reportcards})


class ReportCardCreateView(View):
    def get(self, request):
        form = ReportcardForm()
        return render(request, 'reportcard/report_form.html', {'form': form})

    def post(self, request):
        form = ReportcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'reportcard/report_form.html', {'form': form})

class ReportCardUpdateView(View):
    def get(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        form = ReportcardForm(instance=reportcard)
        return render(request, 'reportcard/report_form.html', {'form': form, 'reportcard': reportcard})

    def post(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        form = ReportcardForm(request.POST, instance=reportcard)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'reportcard/report_form.html', {'form': form, 'reportcard': reportcard})

class ReportCardDeleteView(View):
    def get(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        reportcard.delete()
        return redirect('list')

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Reportcard, Student

class ReportCardView(View):
    def get(self, request, pk):
        
        reportcard = Reportcard.objects.get(pk=pk)

        context = {
            'student_name': reportcard.stuname.first_name,
            'total_marks': reportcard.total_marks(),
            'total_grade':reportcard.total_grade(),
            'performance': reportcard.performance(),
        }

        return render(request, 'achieve/reportcard.html', context)
