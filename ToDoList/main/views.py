from django.shortcuts import render,redirect, get_object_or_404
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
    p=name.id
    it=name.items_set.all()
    if request.method=="POST":
        text=request.POST.get("item")

        if text!="":
            name.items_set.create(text=text,complete=False)
            return redirect("list",p)
                
        
    
    return render(request,"list.html",{"name":name.name,"items":it})

def delete_item(request,id):
    item=get_object_or_404(items,id=id)
    item.delete()
    todol=item.todolist.id
    print("hellowww")
    return redirect("list",todol)

def delete_list(request,id):
    todol=get_object_or_404(ToDoList,id=id)
    todol.delete()
    return redirect("home")

def update(request,id):
    text=request.POST.get("newdat")
    print("hello")
    item=get_object_or_404(items,id=id)
    todo=item.todolist.id
    if text!="":
       
        item.text=text
        
        item.save()
        print("text updated")
    else:
        print("empty text")
    return redirect("list",todo)