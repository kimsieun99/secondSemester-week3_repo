from django.shortcuts import render, redirect, get_object_or_404

from wishlistapp.forms import BlogForm
from .models import Blog, Wishlist
from django.contrib.auth.decorators import login_required

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
    already_in_wishlist = False
    if request.user.is_authenticated:
        already_in_wishlist = Wishlist.objects.filter(user=request.user, post=blog).exists()
    return render(request, 'detail.html', {'blog': blog, 'already_in_wishlist': already_in_wishlist})

def wishlist(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    return render(request, 'wishlist.html', {'wishlists':wishlists})

@login_required    
def add_to_wishlist(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    already_in_wishlist = Wishlist.objects.filter(user=request.user, post=post).exists()
    if not already_in_wishlist:
        wishlist_item = Wishlist.objects.create(user=request.user, post=post)
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, post=post)
    wishlist_item.delete()
    return redirect('wishlist')


def writinglist(request):
    user = request.user
    user_blogs = Blog.objects.filter(user=user)
    return render(request, 'writinglist.html', {'user_blogs': user_blogs})