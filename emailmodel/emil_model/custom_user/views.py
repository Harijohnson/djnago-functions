from django.shortcuts import  render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegister
from django.contrib.auth.models import User
# from custom_user import User
def home(request):
    context= {}
    return render(request,"home.html",context=context)


def signup_user(request):
    context={}
    if request.method =='POST':
        form  = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['username']
            password1= request.POST['password']
            password2= request.POST['password']
            user = User.create_user(request,username=username,email=email,password1=password1,password2=password2)
            user.save()
            messages.success(request,"Registration successful.")
            return redirect('login-user')
        messages.error(request,"Unsuccessful registration. Invalid information.")
    context['form'] = UserRegister()
    return render (request=request, template_name="signup.html", context=context)

def login_user(request):
    context={}
    if request.method == 'POST':
        form = UserRegister(request,request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    context['form'] = UserRegister()
    return render(request=request, template_name="login.html", context=context)



def logout_user(request):
    if request.method=="POST":
        login(request)
        return redirect('home')
