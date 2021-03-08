from django.shortcuts import render
from .models import render

# Create your views here.
def user_list(req):
    users = Artist.objects.all()
    return render(req, 'asc/user_list.html', {'users': users})

def user_detail(req, pk):
    user = User.objects.get(id=pk)
    return render(req, 'asc/user_detail.html', {'user': user})

def post_list(req):
    posts = Post.objects.all()
    return render(req, 'asc/post_list.html', {'posts': posts})

