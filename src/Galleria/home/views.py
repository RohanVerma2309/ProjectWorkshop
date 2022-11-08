from django.shortcuts import render, HttpResponse
from home.models import *

# Create your views here.
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