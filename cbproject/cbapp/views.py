from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import createUserForm
from .decorators import unauthenticated_user
from .forms import Roomform
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    domain = Domain.objects.all()
    rooms=Room.objects.all()
    topics=Topic.objects.all()
    
    room_count = rooms.count()

    # room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'domain':domain}
    return render(request,"cbapp/home.html",context)


@unauthenticated_user
def signup(request):
    
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request,"cbapp/signup.html",context)


@unauthenticated_user
def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.info(request,"Username or Password is incorrect")
            return redirect('login')
    
    return render(request,"cbapp/login.html")

def logout_user(request):
    logout(request)
    return redirect('/')


def createRoom(request):
   
    form=Roomform()
    if request.method=='POST':
        '''print(request.POST)'''
        form=Roomform(request.POST)
        if form.is_valid():
            form.save()
            form.save()
        return redirect("home")
    context={'form':form}
    return render(request,'cbapp/create-room.html',context)


def updateRoom(request,pk):
    rooms = Room.objects.get(id=pk)
    form=Roomform(instance=rooms)
    if request.method=='POST':
        '''print(request.POST)'''
        form=Roomform(request.POST,instance=rooms)
        if form.is_valid():
            form.save()
        return redirect("home")
    context={'form':form}
    return render(request,'cbapp/create-room.html',context)

def deleteRoom(request,pk):

    rooms = Room.objects.get(id=pk)
    if request.method == 'POST':
        rooms.delete()
        return redirect('home')
   
   
    context={'obj':rooms}
    return render(request,'cbapp/delete.html',context)




