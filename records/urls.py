from django.urls import include, path   # importing module include and path
from . import views    # importing views
from django.contrib import admin

urlpatterns = [
    path('register', views.register, name='register'),
    # path given to python  to follow this route
    path('login', views.login, name='login'),
    # path given to python  to follow this route
    path('logout', views.logout, name='logout'),


]
