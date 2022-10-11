from pydoc import describe
from tkinter import Place

from urllib import request

from django.shortcuts import render



from .models import Destinations,comment

from django.core.cache import cache


def details(request):
    id=request.GET['id']
    if cache.get(id):
        pro=cache.get(id)
        print("data come from cache")
    else:
        pro=Destinations.objects.get(id=id)
        cache.set(id,pro)
        print("data from database")
    cmt=comment.objects.filter(place_id=id)#for comments loading 
    print(pro)
    res=render(request,'single.html',{'pro':pro,'cmt':cmt})
    res.set_cookie('pro_name',pro.name)
    return res


def commenting(request):
    name=request.GET["user"]
    msg=request.GET["msg"]
    pro=request.GET["pro_id"]
    cmt=comment.objects.create(name=name,cmt=msg,place_id=pro)#for adding  new comments
    cmt.save();
    return render(request,'test.html')

def searching(request):
    val=request.POST["srh"]
    obj=Destinations.objects.filter(name__istartswith=val)
    print(obj)

    return render(request,'test.html',{'srh':val})


def details2(request):
    id=request.GET['id']
    pro=Destinations.objects.get(id=id)


    if "recent" in request.session:
        
        if id in request.session["recent"]: 
            request.session["recent"].remove(id)#removing repeating product


        request.session['recent'].insert(0,id)
        if len(request.session["recent"])>4:
            request.session["recent"].pop()
        print(request.session['recent'])
        place=Destinations.objects.filter(id__in=request.session['recent'])
        print(place)

 
    else:
        request.session["recent"]=[id]
        place=Destinations.objects.filter(id=id)
    request.session.modified=True      #session modification

    cmt=comment.objects.filter(place_id=id)

    return render(request,'single.html',{'pro':pro,'cmt':cmt,'place':place})