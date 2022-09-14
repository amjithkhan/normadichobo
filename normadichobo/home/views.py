
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from home.models import product


from product.models import Destinations




def index(request):
    data=Destinations.objects.all()
    d=data



    return render(request,'index.html',{'da':data})

def content(product):
    cont="p1"
    return render(product,'registration.html',{'uk':pro})

def login(request):
    return render (request,'login.html')

def registration(request):
    return render (request,'registration.html')


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
    uname=request.GET['uname']
    fname=request.GET['fname']
    lname=request.GET['lname']
    ename=request.GET['email']
    pname=request.GET['pname']
    p2name=request.GET['p2name']
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




