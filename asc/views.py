from rest_framework import generics
from .serializers import PostSerializer, UserSerializer
from .models import Post, User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# from django.shortcuts import render, redirect
# from .models import User, Post
# from .forms import UserForm

# Create your views here.
# def user_list(req):
#     users = User.objects.all()
#     return render(req, 'asc/user_list.html', {'users': users})

# def user_detail(req, pk):
#     user = User.objects.get(id=pk)
#     return render(req, 'asc/user_detail.html', {'user': user})

# def post_list(req):
#     posts = Post.objects.all()
#     return render(req, 'asc/post_list.html', {'posts': posts})

# def post_detail(req, pk):
#     post = Post.objects.get(id=pk)
#     return render(req, 'asc/post_detail.html', {'post': post})

# def user_create(req):
#     if req.method == 'POST':
#         form = UserForm(req.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm()
#     return render(req, 'asc/user_form.html', {'form': form})

# def post_create(req):
#     if req.method == 'POST':
#         form = PostForm(req.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(req, 'asc/post_form.html', {'form': form})

