from django.contrib.auth.models import User
from django.contrib import messages ,auth
from django.shortcuts import redirect, render
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Exists")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print("User created")
                return redirect('login')
                
            
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
