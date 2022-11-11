"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from listings import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('admin/', admin.site.urls),
path('home/', views.home, name='home'),
path('subscribe/', views.subscribe),
path('flux/', views.flux, name='flux'),
path('contact-us/', views.contact),
path('abonnements/', views.abonnements, name='abonnements'),
path('tickets/', views.tickets, name='tickets'),
path('tickets-modify/', views.ticketsModify),
path('critics/', views.critics, name='critics'),
path('critics-response/', views.criticsResponse),
path('critics-modify/', views.criticsModify),
path('your-posts/', views.yourPosts, name='yourposts'),
path('base/', views.base)
]


