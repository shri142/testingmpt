from audioop import reverse
import genericpath
from sre_constants import SUCCESS
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def Adminpage(request):
    user = Profile.objects.all()
    context = {'user': user} 
    return render(request, 'admin.html', context)

# def faculty(request):
#     user = User.objects.all()
#     context = {'user': user}
#     return render(request, 'faculty-dashboard.html', context)

def student(request):
    return render(request, 'student-dashboard.html')

def faculty(request):
    return render(request, 'faculty-dashboard.html')
    

def studentdetail(request, pk):
    user = Profile.objects.get(id=pk)
    context = {'users': user}
    return render(request, 'student-profile.html', context)


def stud_prof(request):
    return render(request, 'student-profile.html')
