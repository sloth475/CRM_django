from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from . import views


urlpatterns = [
    #path('', admin.site.urls),
    path ('', views.home),
    path('contact/',views.contact),

]