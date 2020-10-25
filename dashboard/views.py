from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from form.models import Form, Response, ResponseQuestion, InputField

# Create your views here.
def view_submission(request, form_id, submission_id):
    # authenticate user to see if the user is the owner of the form
    form = Form.objects.get(id=form_id)
    # resp = Response.objects.get(id=submission_id)
    rs = Response.objects.filter(form_id=form_id)[::-1]
    rs2 = [] # [[Response, index #]]
    i = 1
    for r in rs:
        rs2.append([r, i])
        i+=1
    resp_qs = ResponseQuestion.objects.filter(response_id=submission_id)
    data = [] # [["label", "input"]]
    for r in resp_qs:
        i = InputField.objects.get(id=r.question_id)
        data.append([i.label, r.response])
    return render(request, "dashboard/view-response.html", {
        "data": data,
        "rs": rs2,
        "f": form
    })


def main_dashboard(request):
    f = Form.objects.filter(user_id=request.user.id)
    return render(request, "dashboard/index.html", {
        "forms": f
    })


def view_form(request, form_id):
    f = Form.objects.get(user_id=request.user.id)
    q = InputField.objects.filter(form_id=form_id)
    return render(request, "dashboard/form.html", {
        "questions": q,
        "f": f
    })


def view_all_submission(request, form_id):
    try:
        r = Response.objects.filter(form_id=form_id)[::-1][0]
    except:
        return HttpResponse("No response, yet...")
    return HttpResponseRedirect(f"/d/{form_id}/{r.id}/")
