from django.shortcuts import render

def home(request):
    return render(request, 'Login/Home.html')

def login(request):
    return render(request, 'Login/Login.html')