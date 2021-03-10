from django.shortcuts import render, redirect
from .models import User, Post
from .forms import UserForm

# Create your views here.
def user_list(req):
    users = User.objects.all()
    return render(req, 'asc/user_list.html', {'users': users})

def user_detail(req, pk):
    user = User.objects.get(id=pk)
    return render(req, 'asc/user_detail.html', {'user': user})

def post_list(req):
    posts = Post.objects.all()
    return render(req, 'asc/post_list.html', {'posts': posts})

def post_detail(req, pk):
    post = Post.objects.get(id=pk)
    return render(req, 'asc/post_detail.html', {'post': post})

def user_create(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(req, 'asc/user_form.html', {'form': form})

