from django.db import models
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.utils import timezone

class MentorProfile(models.Model):
    gender_choices= [
        ('Male', 'Male'),
        ('Female' , 'Female'),
    ]

    branch_choices = [
        ('Computer Engineering', 'Computer Engineering'),
        ('Electronics and Telecommunication Engineering',
         'Electronics and Telecommunication Engineering'),
        ('Information Technology', 'Information Technology'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
    ]

    Blood_grp_choices=[
        ('A+','A+'),
        ('B+','B+'),
        ('O+','O+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('B-','B-'),
        ('O-','O-'),
        ('AB-','AB-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DateofBirth= models.DateField(max_length=50, null=True)
    Gender = models.CharField(max_length=50, null=True, choices=gender_choices)
    Blood_grp = models.CharField(max_length=50, null=True, choices=Blood_grp_choices )
    Branch = models.CharField(max_length=70, null=True, choices=branch_choices)
    city = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    # MentorId = models.IntegerField(primary_key=True, default=True)

    def __str__(self):
        return self.user.first_name+ ' ' +self.user.last_name



class StudentProfile(models.Model):
    gender_choices= [
        ('Male', 'Male'),
        ('Female' , 'Female'),
    ]

    branch_choices = [
        ('Computer Engineering', 'Computer Engineering'),
        ('Electronics and Telecommunication Engineering',
         'Electronics and Telecommunication Engineering'),
        ('Information Technology', 'Information Technology'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
    ]

    Blood_grp_choices=[
        ('A+','A+'),
        ('B+','B+'),
        ('O+','O+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('B-','B-'),
        ('O-','O-'),
        ('AB-','AB-'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)
    current_rollNo = models.IntegerField(unique=True, null=True)
    AimForLife = models.CharField(max_length=100, blank=True, null=True)
    reason_of_engg = models.CharField(max_length=50, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    Course = models.CharField(max_length=50, blank=True, null=True)
    YearOfAdmission = models.IntegerField(null=True)
    department = models.CharField(max_length=50, null=True)
    DateofBirth= models.DateField(max_length=50, null=True)
    Gender = models.CharField(max_length=50, null=True, choices=gender_choices)
    Blood_grp = models.CharField(max_length=50, null=True, choices=Blood_grp_choices )
    Branch = models.CharField(max_length=70, null=True, choices=branch_choices)
    city = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    Mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.user.first_name+ ' ' + self.user.last_name


    