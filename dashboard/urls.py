from django.urls import path
from . import views

urlpatterns = [
    path("<str:form_id>/submissions/", views.view_all_submission),
    path("<str:form_id>/<str:submission_id>/", views.view_submission), # /d/<form>/<sub>/,
    path("", views.main_dashboard),
    path("<str:form_id>/", views.view_form),
]