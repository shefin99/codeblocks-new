from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import createUserForm
from .decorators import unauthenticated_user
from .forms import Roomform
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    domain = Domain.objects.all()
    events = Events.objects.all()
    rooms=Room.objects.filter(
        Q(topic__name__contains=q) |
        Q(name__icontains=q) |
        Q(desc__icontains=q) 
        )
    topics=Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    # room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'domain':domain,'events':events,'room_messages':room_messages}
    return render(request,"cbapp/index.html",context)


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


@login_required(login_url='login')
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
            
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {'room':room,'room_messages':room_messages,'participants':participants}

    return render(request,"cbapp/room.html",context)

@login_required(login_url='login')
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
    return render(request,'cbapp/roomform.html',context)

@login_required(login_url='login')
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
    return render(request,'cbapp/roomform.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):

    rooms = Room.objects.get(id=pk)
    if request.method == 'POST':
        rooms.delete()
        return redirect('home')
   
   
    context={'obj':rooms}
    return render(request,'cbapp/delete.html',context)



@login_required(login_url='login')
def deleteMessage(request,pk):
   
    message=Message.objects.get(id=pk)

    if request.user!=message.user:
        return HttpResponse("you are not allowed here....")
    
    if request.method=='POST':
        message.delete()
        return redirect('/')
    context = {'obj':message}
    return render(request,'cbapp/delete.html',context)

