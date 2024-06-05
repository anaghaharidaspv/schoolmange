import datetime
from time import timezone
from django.db import models
from adminapp.models import *

# Create your models here.
class UploadFile(models.Model):
  filename=models.CharField(max_length=50)
  upload_file=models.FileField(upload_to='media/')
  courses = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
  batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)
  
  def __str__(self):
    return self.filename

class excelupload(models.Model):
  name=models.CharField(max_length=100)
  dob=models.CharField(max_length=10)
  phone=models.CharField(max_length=10)
  
  def __str__(self):
    return self.name
  

class Achievement(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    PERFORMANCE_CHOICES = [
        ('Good', 'Good'),
        ('Bad', 'Bad'),
        ('Average', 'Average'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    class_performance = models.CharField(max_length=7, choices=PERFORMANCE_CHOICES)
    
    
    def save(self, *args, **kwargs):
        # Calculate grade based on score
        if self.score >= 90:
            self.grade = 'A'
        elif self.score >= 80:
            self.grade = 'B'
        elif self.score >= 70:
            self.grade = 'C'
        elif self.score >= 60:
            self.grade = 'D'
        else:
            self.grade = 'E'

        # Calculate class performance based on grade
        if self.grade in ['A', 'B']:
            self.class_performance = 'Good'
        elif self.grade == 'C':
            self.class_performance = 'Average'
        else:
            self.class_performance = 'Bad'

        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f'{self.student.name} - {self.grade} - {self.class_performance}'

    def __str__(self):
        return f'{self.student.name} - {self.grade} - {self.class_performance}'
 
     
     

