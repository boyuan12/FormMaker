from django.shortcuts import render
from .models import Form, InputField
from django.http import HttpResponse

# Create your views here.
def create(request):
    if request.method == "POST":
        Form(name=request.POST["form-name"]).save()
        f = Form.objects.filter(name=request.POST["form-name"])[::-1][0]
        for i in range(int(request.POST["questionCount"])):
            InputField(label=request.POST[str(i)], form_id=f.id).save()
        return HttpResponse("success")
    else:
        return render(request, "form/create.html")