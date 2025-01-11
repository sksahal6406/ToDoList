from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    t=ToDoList.objects.all()
    return render(request,"home.html",{"t":t})

def create(request):
    if request.method=="POST":
        n=request.POST.get("name")
        t=ToDoList(name=n)
        t.save()
        # request.user.todolist.add(t)
        print(t.name)
        return redirect("home")

    else:
        print("not caught")
    return render(request,"create.html",{})

def list(request,id):
    name=ToDoList.objects.get(id=id)
    it=name.items_set.all()
    if request.method=="POST":
        text=request.POST.get("item")
        if request.POST.get("newItem"):
            if text!="":
                name.items_set.create(text=text,complete=False)
                
        if request.POST.get("del"):
            
            for item in name.items_set.all():
                print(request.POST.get(str(item.id)))
                if request.POST.get(str(item.id))=="del":
                    name.items_set.remove(item)
            
   
    return render(request,"list.html",{"name":name.name,"items":it})

def delete(request,id):
    
    return render()