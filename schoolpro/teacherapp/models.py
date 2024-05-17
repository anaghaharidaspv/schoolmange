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