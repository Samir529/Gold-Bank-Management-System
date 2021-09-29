from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include

app_name = 'goldbankapp'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    ]