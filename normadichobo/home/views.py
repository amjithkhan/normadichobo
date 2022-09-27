
from http.client import HTTPResponse
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from home.models import product


from product.models import Destinations
from django.contrib.auth.models import User,auth



def index(request):
    data=Destinations.objects.all()
    d=data



    return render(request,'index.html',{'da':data})

def content(product):
    cont="p1"
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        name=request.POST['lnmae']
        email=request.POST['email']
        pname=request.POST['pname']
        p2name=request.POST['p2name']
        ucheck=User.objects.filter(username=uname)
        echeck=User.objects.filter(ename=email)
        if ucheck:
            msg="username is already existed"
    
            return render (request,'registration.html')
        elif echeck:
            msg="email is already existed"
            return render (request,'registration.html')
        elif pname!=p2name:
            msg="password is incorrect"
            return render (request,'registration.html')


def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pname=request.POST['pname']
        user=auth.authenticate(username=uname,password=pname)
        if user is not None:
           auth.login(request,user)
           return redirect('/')
        else:
           return render (request,'test.html',{'key1':'invalid username and password'})

    else:
        
       return render (request,'login.html')




def registration(request):
    if request.method=="POST":

       fname=request.POST['fname']
       lname=request.POST['lname']
       uname=request.POST['uname']
       ename=request.POST['email']
       pname=request.POST['pname']
       p2name=request.POST['p2name']
       ucheck=User.objects.filter(username=uname)
       echeck=User.objects.filter(email=ename)
       if ucheck:
          return render(request,'test.html',{'msg':'username is already taken'})
       elif echeck: 
          return render(request,'test.html',{'msg':'email is already taken'})
       elif pname != p2name:
          return render(request,'test.html',{'msg':'incorrect password'})
       else:
          user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=pname)
          user.save();
          return redirect('/')
    else:


        return render (request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def loginsub(request):
    uname=request.GET['uname']
    pname=request.GET['pname']
    user=auth.authenticate(username=uname,password=pname)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        return render (request,'test.html',{'key1':'invalid username and password'})
        
        
def registersub(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    uname=request.POST['uname']
    ename=request.POST['email']
    pname=request.POST['pname']
    p2name=request.POST['p2name']
    ucheck=User.objects.filter(username=uname)
    echeck=User.objects.filter(email=ename)
    if ucheck:
        return render(request,'test.html',{'msg':'username is already taken'})
    elif echeck: 
        return render(request,'test.html',{'msg':'email is already taken'})
    elif pname != p2name:
        return render(request,'test.html',{'msg':'incorrect password'})
    else:
        user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=pname)
        user.save();
    
def comment(request):
    

        return redirect('/')




