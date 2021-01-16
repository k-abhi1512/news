from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.Authentication(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def listng(request):
    return render(request, 'insert.html')


def home(request):
    return render(request, 'home.html')
