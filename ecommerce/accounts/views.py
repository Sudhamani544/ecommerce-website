from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.authenticate(username = username, passwod=password)

        if user is not None:
            auth.login(request)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.info(request,'password is not matching')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'username exists')
            return redirect('register')
            print('went wrong')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email exists')
            return redirect('login')
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
            user.save()
            messages.info(request,'user created')
            return redirect('register')
        return redirect('http://127.0.0.1:8000/')
    else:
        return render(request,'accounts/register.html')

def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/')
