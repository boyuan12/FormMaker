from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create),
    path("v/<str:form_id>/", views.view_form),
    path("s/<str:form_id>/", views.submit_form),
]