from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from .models import Product,Profile
# Create your views here.

def Homepage(request):
    return render(request, 'index.html')

def Productpage(request):
    item = Product.objects.all()

    context = {
        'data':item
    }
    return render(request, 'product.html',context) 

def user_log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('user not found')    
    return render(request, 'login.html')  

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')    
    else:        
        form = RegisterForm
    return render(request, 'register.html',{"form":form}) 

def profile(request):
    
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
   
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'u_form': p_form,
        'user_profile':user_profile
    }

    return render(request, 'profile.html',context)    
