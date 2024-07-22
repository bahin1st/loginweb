from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from .forms import LoginForm , RegisterForm,HouseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import House
from django.core.paginator import Paginator

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
                return redirect('/house_list')
        
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

@login_required(login_url='login')
def main_view(request):
    return render(request,'house_list')



def logout_view(request):
    logout(request)
    return redirect('house_list')



def logout_view(request):
    logout(request)
    return redirect('login')





from .forms import ProfileForm,HouseImageFormSet
from .models import Profile

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

@login_required
def edit_house(request, house_id):
   
    house = get_object_or_404(House, id=house_id)
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('housedetail', id=house_id)  # Redirect to house detail page
    else:
        form = HouseForm(instance=house)
    
    return render(request, 'edit_house.html', {'form': form, 'house': house})

@login_required
def register_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        formset = HouseImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            formset.instance = house
            formset.save()
            return redirect('house_list')
    else:
        form = HouseForm()
        formset = HouseImageFormSet()
    return render(request, 'register_house.html', {'form': form, 'formset': formset})

# def house_list(request):
#     house_list = House.objects.all()
#     paginator=Paginator(house_list,4)
#     page_number = request.GET.get('page')
#     houses = paginator.get_page(page_number)
#     return render(request, 'house_list.html', {'houses': houses})

# views.py
from .forms import HouseFilterForm

def house_list(request):
    house_list = House.objects.all()
    
    filter_form = HouseFilterForm(request.GET)
    if filter_form.is_valid():
        min_price = filter_form.cleaned_data.get('min_price')
        max_price = filter_form.cleaned_data.get('max_price')
        property_type = filter_form.cleaned_data.get('property_type')
        status = filter_form.cleaned_data.get('status')
        min_rooms = filter_form.cleaned_data.get('min_rooms')
        max_rooms = filter_form.cleaned_data.get('max_rooms')
        min_area = filter_form.cleaned_data.get('min_area')
        max_area = filter_form.cleaned_data.get('max_area')
        country=filter_form.cleaned_data.get('country')
        
        if min_price:
            house_list = house_list.filter(price__gte=min_price)
        if max_price:
            house_list = house_list.filter(price__lte=max_price)
        if property_type:
            house_list = house_list.filter(property_type=property_type)
        if status:
            house_list = house_list.filter(status=status)
        if country:
            house_list = house_list.filter(country=country)

        if min_rooms:
            house_list = house_list.filter(rooms_count__gte=min_rooms)
        if max_rooms:
            house_list = house_list.filter(rooms_count__lte=max_rooms)
        if min_area:
            house_list = house_list.filter(area__gte=min_area)
        if max_area:
            house_list = house_list.filter(area__lte=max_area)

    paginator = Paginator(house_list, 4)  # Paginate by 4 houses per page
    page_number = request.GET.get('page')
    houses = paginator.get_page(page_number)
    
    return render(request, 'house_list.html', {'houses': houses, 'filter_form': filter_form})


def housecliked(request,id):
    house = House.objects.get(id=id)
    form = HouseForm(request.POST, instance=house)
    context={'house':house, 
             'form': form}
    return render(request,'thehouse.html',context)

@login_required
def property_delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST' and request.user == house.owner:
        house.delete()
        return redirect('house_list')
    return redirect('house_list', pk=pk)