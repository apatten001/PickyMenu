"""Pickymenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from restaurants.views import *
from django.contrib.auth.views import LoginView, LogoutView
from profiles.views import ProfileFollowToggle, RegisterView
from menus.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('follow/', ProfileFollowToggle.as_view(), name='follow'),
    path('restaurants/', include('restaurants.urls', namespace='restaurants')),
    path('items/', include('menus.urls', namespace='menu')),
    path('profile/', include('profiles.urls', namespace='profiles')),


]
