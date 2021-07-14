from django.shortcuts import render
from .models import post
# from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'blogApp/home.html', context)

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})
