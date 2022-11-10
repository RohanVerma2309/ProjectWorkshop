from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image, ImageShow
from django.views.generic import DetailView

def showImage(request):
    image = Image.objects.all()
    photos = ImageShow.objects.all()
    data = {
        'image' : image,
        'photos': photos,
    }
    return render(request,"users/home.html",data)



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def home(request):
    img = Image.objects.all()
    return render(request, 'users/home.html', {'img':img})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'users/upload.html', {'img':img, 'form':form})