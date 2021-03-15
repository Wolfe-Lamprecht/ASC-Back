from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),

    # path('', views.user_list, name='user_list'),
    # path('users', views.user_list, name='user_list'),
    # path('posts', views.post_list),
    # path('users/<int:pk>', views.user_detail, name='user_detail'), 
    # path('posts/<int:pk>', views.post_detail, name='post_detail'),
]