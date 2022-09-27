from pydoc import describe
import re
from urllib import request
from django.shortcuts import render
from .models import Destinations,comment



def details(request):
    id=request.GET['id']
    pro=Destinations.objects.get(id=id)
    print(pro)
    cmt=comment.objects.filter(place_id=id)
    return render(request,'single.html',{'pro':pro,'cmt':cmt})

def commenting(request):
    name=request.GET["user"]
    msg=request.GET["msg"]
    pro=request.GET["pro_id"]
    cmt=comment.objects.create(name=name,cmt=msg,place_id=pro)
    cmt.save();
    
    return render(request,'test.html')