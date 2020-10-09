from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("verify/<str:token>/", views.verify),
    path("forgot-password/", views.forgot_password),
    path("reset-password/<str:token>/", views.reset_password)
]