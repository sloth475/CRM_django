from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse ("this is home page")

def contact(request):
    return HttpResponse('this is contact page')

# Create your views here.
