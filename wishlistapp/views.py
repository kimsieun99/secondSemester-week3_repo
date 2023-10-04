from django.shortcuts import render, redirect, get_object_or_404

from wishlistapp.forms import BlogForm
from .models import Blog


# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # 현재 로그인된 사용자를 할당
            post.save()
            return redirect('read')
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form': form})

def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs': blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'detail.html', {'blog': blog})