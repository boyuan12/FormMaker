from django.shortcuts import redirect, render
from .models import Form, InputField, Response, ResponseQuestion
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def create(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("")
        Form(name=request.POST["form-name"], user_id=request.user.id).save()
        f = Form.objects.filter(name=request.POST["form-name"])[::-1][0]
        print(f)
        for i in range(int(request.POST["questionCount"])):
            try:
                InputField(label=request.POST[str(i)], form_id=f.id).save()
            except Exception as e:
                print(str(e))
        return HttpResponse("success")
    else:
        return render(request, "form/create.html")


def view_form(request, form_id):
    try:
        f = Form.objects.get(id=form_id)
    except:
        return HttpResponse("404 Not Found")

    inputs = InputField.objects.filter(form_id=f.id)
    print(inputs)

    return render(request, "form/view-form.html", {
        "form_id": form_id,
        "inputs": inputs
    })


def submit_form(request, form_id):
    Response(user_id=request.user.id, form_id=form_id).save()
    r = Response.objects.filter(user_id=request.user.id, form_id=form_id)[::-1][0]
    for i in request.POST:
        if i == "csrfmiddlewaretoken":
            continue
        ResponseQuestion(question_id=i, response=request.POST[i], response_id=r.id).save()
    return HttpResponse("success")