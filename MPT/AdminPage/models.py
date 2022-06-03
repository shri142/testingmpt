from time import timezone
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password,  **other_fields):
        user = self.model(email=email, username = username, first_name=first_name, last_name=last_name, **other_fields )
        user.set_password(password)
        user.save
        return user

    def create_superuser(self, email, username, first_name, last_name, password,  **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        return self.create_user(email, username , first_name, last_name, password, **other_fields)

    def authenticate(self, username, password):
        user= Profile.objects.all(username=username, password=password)
        return user



class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    about = models.TextField(max_length=500, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=10, null=True)
    course = models.CharField(max_length=20, null=True)
    YearOfAdmission = models.IntegerField( null=True)
    current_RollNo = models.IntegerField( null=True)
    AimForLife = models.CharField(max_length=250, null=True)
    Reason_of_eng = models.CharField(max_length=20, null=True)
    updated = models.DateTimeField(auto_now=True)

    objects= AccountManager()
    USERNAME_FIELD = 'email'

    #for superusers the following fields are req
    REQUIRED_FIELDS= ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username