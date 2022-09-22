from pydoc import describe
from urllib import request
from django.shortcuts import render
from .models import Destinations



def details(request):
    id=request.GET['id']
    pro=Destinations.objects.get(id=id)
    print(pro)
    return render(request,'single.html',{'pro':pro})

