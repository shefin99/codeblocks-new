from django.shortcuts import render,redirect
from . models import Domain
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import createUserForm
# Create your views here.


def home(request):
    domain = Domain.objects.all()
    context={'domain':domain}
    return render(request,"cbapp/home.html",context)


def signup(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    context = {'form':form}
    return render(request,"cbapp/signup.html",context)


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


