from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from django.contrib import messages
import threading 
from sendPdfs.views import mergeAndSend


def homePage(request):
    return render(request,'loginPage/login.html',{}) 
    
def submit_login(request):
    # כפתור התחברות אחרי שהכנסנו נתונים
    userName=request.POST.get('username', None)
    password=request.POST.get('password', None)
    user=User.objects.filter(userName=userName).filter(password=password)
    if not user:
        return render(request,'loginPage/login.html',{})
    global now_user
    now_user=user[0]
    global t
    t = threading.Thread(target=mergeAndSend,args=(now_user,))
    t.start()
    return render(request,f'users/client.html',{'user':(user[0])}) 

def submit_registration(request):
    #כפתור הרשמה אחרי שמלאנו פרטים 
    user=User()
    user.firstName=request.POST['firstName']
    user.lastName=request.POST['lastName']
    user.userName=request.POST['userName']
    user.password=request.POST['password']
    user.email=request.POST['Email']
    user.phoneNumber = request.POST['phoneNumber']
    user.phoneNumber = '+972'+ user.phoneNumber[1:]
    print(user.phoneNumber)
    userTest=User.objects.filter(userName=user.userName)
    if userTest :
        #הודעה שהשם משתמש כבר תפוס
        messages.success(request, 'User Already In Registered')
        return render(request,'registerPage/register.html',{})
    user.save()
    return render(request,'loginPage/login.html',{}) 
def getNowUser():
    return now_user

