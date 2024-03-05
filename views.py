from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
# Create your views here.

#def About(request):
    #return render(request,'about.html'
def About(request):
    return render(request,"about.html")
def test(request):
    return render(request,"test.html")


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def login(request):
    error=""
    if request.method=='Post':
        U = request.post['uname']
        p = request.post['pwd']
        user = authenticate(username=U,password=p)
        try:
         if user.is_staff:
        login(request,user)
        error="no"
    else:
        error="yes"
        except:
        error = "yes"
        d = {'error':error}
    return render(request,'index.html',d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

