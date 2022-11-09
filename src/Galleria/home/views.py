from django.shortcuts import render, HttpResponse, redirect
from home.models import *
from django.contrib.auth.forms import UserCreationForm
# from .form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def index(request):
    category = Category.objects.all()
    images = Image.objects.all()
    data = {
        'category': category,
        'images': images,
        }
    return render(request, "home.html", data)

def showCategoryPage(request, cid):
    category = Category.objects.all()
    filteredCategory = Category.objects.get(pk = cid)
    images = Image.objects.filter(category = filteredCategory)
    data = {
        'category': category,
        'images': images,
        }
    return render(request, "home.html", data)