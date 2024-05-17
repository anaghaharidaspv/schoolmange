from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User


# Create your models here.
class adminmodel(AbstractBaseUser):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Teacher(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name



class Student(User):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    courses=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='student_course')
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='student_batch')
    def __str__(self):
        return self.first_name

    