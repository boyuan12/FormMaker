from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        login(request, user)
        return HttpResponse("Hello! You logged in successfully!")
    else:
        return render(request, "authentication/register.html")


def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponse("Hello! You logged in successfully!")
        return HttpResponse("You entered wrong credentials")
    else:
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return HttpResponse("You logged out successfully!")