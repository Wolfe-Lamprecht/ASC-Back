from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('', views.post_list),
    path('users/<int:pk>', views.user_detail, name='user_detail'), 
]