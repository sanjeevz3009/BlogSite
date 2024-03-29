from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'blogApp/home.html', context)

class PostListView(ListView):
    model = post
    template_name = 'blogApp/home.html' #<app><model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-datePosted']
    paginate_by = 8
    
class UserPostListView(ListView):
    model = post
    template_name = 'blogApp/user_posts.html' #<app><model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-datePosted']
    paginate_by = 8
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-datePosted')
    
    
class PostDetailView(DetailView):
    model = post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})
