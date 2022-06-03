from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import login
from AdminPage.models import Profile


def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = Profile.objects.authenticate(username, password)
        print("user", user)
        # if user is not None:
        if user:
            login(request, user)
            if request.user.is_staff:
                return redirect('/facultydashboard')
               
            else:
                return redirect('/studentdashboard')
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'login-page.html')

    else: 
        return render(request, 'login-page.html')