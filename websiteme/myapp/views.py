from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from .forms import LoginForm , RegisterForm,HouseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import House

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('coming/')
        
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

@login_required(login_url='login')
def main_view(request):
    return render(request,'coming.html')



def logout_view(request):
    logout(request)
    return redirect('login')



def some_view(request):
    request.session['custom_data'] = 'some_value'  #

    custom_data = request.session.get('custom_data')
    return render(request, 'datacustom.html', {'custom_data': custom_data})

def clear_session_data(request):
    if 'custom_data' in request.session:
        del request.session['custom_data']
    return redirect('/data')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render


def logout_view(request):
    logout(request)
    return redirect('login')




# 
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})


def register_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            return redirect('house_list')
    else:
        form = HouseForm()
    return render(request, 'register_house.html', {'form': form})

def edit_house(request, house_id):
    house = get_object_or_404(House, id=house_id)
    if request.method == 'POST':
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = HouseForm(instance=house)
    
    return render(request, 'edit_house.html', {'form': form})

def house_list(request):
    houses = House.objects.filter(owner=request.user)
    return render(request, 'house_list.html', {'houses': houses})

def housecliked(request,id):
    house = House.objects.get(id=id)
    context={'house':house}
    return render(request,'thehouse.html',context)