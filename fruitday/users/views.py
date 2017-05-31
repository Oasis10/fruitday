from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'users/index.html')

def index2(request):
    return redirect('/')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')
