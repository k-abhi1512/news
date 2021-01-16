from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

# login view function
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid user credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

# Insert listing view function
def listng(request):

    newsForm = InsertPageForm()

    if request.method == 'POST':
        newsForm = InsertPageForm(request.POST, request.FILES)
        if newsForm.is_valid():
            newsForm.save()
            messages.success(request, 'New News Listing Added')

    context = {'form': newsForm}
    return render(request, 'insert.html', context)

# home page view function
def home(request):
    news = InsertPage.objects.all()
    context ={'news':news}
    return render(request, 'home.html', context)

# a logout function
def logout(request):
    auth.logout(request)
    return redirect('home')