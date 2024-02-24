from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'company_index.html')

def registration(request):
    return render(request, 'company_registration.html')

def login(request):
    return render(request, 'company_login.html')

def profile(request):
    return render(request, 'company_profile.html')