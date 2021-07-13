from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Sanjeev Srithevan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 21, 2018'
    },
    {
        'author': 'Mehmet Mazi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogApp/home.html', context)

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})
