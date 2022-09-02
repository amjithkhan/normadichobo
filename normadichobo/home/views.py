import email
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from home.models import product
from.models import product
from django.contrib.auth.models import User,auth


p1=product()
p1.name="Macbook"
p1.price=1500000
p1.desc="MacBook Pro. Our most powerful notebooks. Fast M1 processors, incredible graphics, and spectacular Retina displays. Now available in a 14-inch model"

p2=product()
p2.name="Pixel6pro"
p2.price=1300000
p2.desc="Google Pixel 6 Pro ; Resolution, 1440 x 3120 pixels, 19.5:9 ratio (~512 ppi density) ; Protection, Corning Gorilla Glass Victus ; Platform, OS ; Chipset, Google"

p3=product()
p3.name="Arrow"
p3.price=3499
p4=product()
p4.name="pan america"
p4.price=5400000
p4.desc="Informed by H-D's touring legacy, Pan America™ is designed to maintain high-speed ride and handling performance even when at the limit of its luggage and weight ."


pro=[p1,p2,p3,p4]


def index(request):
    return render(request,'index.html')

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




