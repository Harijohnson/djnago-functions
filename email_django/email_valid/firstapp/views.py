from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context={}
    return render (request,'base.html',context=context)

def signup_user(request):
    context={}
    return render (request,'signup.html',context=context)


def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle authentication failure
            return  redirect('login_')

    return render(request, 'login.html')


def logout_user(request):
    context={}
    return render (request,'logout.html',context=context)






































