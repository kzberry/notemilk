"""notemilk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from . import views
from .views import home, login_view, logout_view, register, note_list

urlpatterns = [
    path('', home, name='home'),
    path('registration/login.html', login_view, name='login'),
    path('registration/logout.html', logout_view, name='logout'),
    path('registration/registration.html', register, name='register'),
    path('note_list.html', note_list, name='note_list'),
    path('admin/', admin.site.urls),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]
