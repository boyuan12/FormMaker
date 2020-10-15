from django.urls import path
from . import views

urlpatterns = [
    path("<str:form_id>/<str:submission_id>/", views.view_submission), # /d/<form>/<sub>/
]