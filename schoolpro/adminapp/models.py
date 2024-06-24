from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User


# Create your models here.
class adminmodel(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    password = models.CharField(max_length=10)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        indexes = [
            models.Index(fields=['username']),
        ]


class Course(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
class Batch(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
class Country1(models.Model):
    country_name=models.CharField(max_length=30)
    def __str__(self):
        return self.country_name
    
class State1(models.Model):
    country=models.ForeignKey(Country1,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.state_name
    
class City1(models.Model):
    state=models.ForeignKey(State1,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.city_name



class Teacher(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    country = models.ForeignKey('Country1', on_delete=models.CASCADE)
    state = models.ForeignKey('State1', on_delete=models.CASCADE)
    city = models.ForeignKey('City1', on_delete=models.CASCADE)

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
    date_of_birth = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_course')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='student_batch')
    country = models.ForeignKey(Country1, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State1, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City1, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['date_of_birth']),
            models.Index(fields=['gender']),
            models.Index(fields=['courses']),
            models.Index(fields=['batch']),
            models.Index(fields=['country']),
            models.Index(fields=['state']),
            models.Index(fields=['city']),
        ]
