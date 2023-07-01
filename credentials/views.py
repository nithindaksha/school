from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'add.html')
        else:
            messages.info(request,"invalid credentials")
            return redirect(request,'login')
    return render(request,'login.html')

def register(request):
     if request.method =='POST':
        username=request.POST['username']

        password = request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
           if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')

           else:
               user = User.objects.create_user(username=username,password=password)
               user.save();
               return redirect('login')

        else:
               messages.info(request,"password not matching")
               return redirect('register')

        return redirect('/')
     return render(request,'register.html')


def cs(request):
    return render(request,'cs.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def add(request):
    return render(request,'form.html')


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['DOB']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        messages.info(request, 'Your password has been changed successfully!')
        return HttpResponseRedirect('/')
      #messages.info("Order Confirmed")
                          # return redirect('/')


    return render(request, 'form.html')
