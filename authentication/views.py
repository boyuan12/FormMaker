from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Token
from mail import send_mail


# Create your views here.
def register(request):
    if request.method == "POST":
        User.objects.create_user(username=request.POST["username"], password=request.POST["password"], email=request.POST["email"])
        Token(user_id=User.objects.get(username=request.POST["username"]).id, type=0).save()
        t = Token.objects.get(user_id=User.objects.get(username=request.POST["username"]).id, type=0)
        send_mail(request.POST["email"], "Verify your account!", f"Go here to verify your account: <a href='http://127.0.0.1:8000/auth/verify/{t.id}'>http://127.0.0.1:8000/auth/verify/{t.id}</a>")
        # user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        # login(request, user)
        return HttpResponse("Hello, please check your email for the next step.")
    else:
        return render(request, "authentication/register.html")


def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            try:
                Token.objects.get(user_id=user.id, type=0)
                return HttpResponse("Please verify your email first")
            except:
                pass
            login(request, user)
            return HttpResponse("Hello! You logged in successfully!")
        return HttpResponse("You entered wrong credentials")
    else:
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return HttpResponse("You logged out successfully!")


def verify(request, token):
    try:
        Token.objects.get(id=token).delete()
        return HttpResponse("You successfully verified your account")
    except:
        return HttpResponse("Your token is invalid")