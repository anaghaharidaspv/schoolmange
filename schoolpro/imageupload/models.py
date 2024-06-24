
from django.db import models
from adminapp.models import Student

# Create your models here.
class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    student=models.OneToOneField(Student,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    