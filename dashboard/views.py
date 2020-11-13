from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from form.models import Form, MultipleChoiceField, MultipleChoiceOption, Response, ResponseQuestion, InputField

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
    data = [] # [["label", "input"], [label, user_opt, [MultipleChoiceOption...]]] 0 -> input; 1 -> mc
    for r in resp_qs:
        try:
            i = InputField.objects.get(id=r.question_id)
            data.append([0, i.label, r.response])
        except:
            i = MultipleChoiceField.objects.get(id=r.question_id)
            op = MultipleChoiceOption.objects.get(id=r.response)
            data.append([1, i.label, op, [o for o in MultipleChoiceOption.objects.filter(question_id=r.question_id)]])

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
    f = Form.objects.get(user_id=request.user.id, id=form_id)

    # [[0, InputField], [1, MultipleChoiceField, [MultipleChoiceOption...]]] 0 input; 1 multiple
    questions = []
    inputs = InputField.objects.filter(form_id=f.id)
    multiple = MultipleChoiceField.objects.filter(form_id=f.id)

    for i in inputs:
        questions.insert(i.order, [0, i])

    for i in multiple:
        options = MultipleChoiceOption.objects.filter(question_id=i.id)
        ops = [o for o in options]
        questions.insert(i.order, [1, i, ops])

    return render(request, "dashboard/form.html", {
        "questions": questions,
        "f": f
    })


def view_all_submission(request, form_id):
    try:
        print(Response.objects.filter(form_id=form_id))
        r = Response.objects.filter(form_id=form_id)[::-1][0]
    except Exception as e:
        return HttpResponse("No response, yet...")
    return HttpResponseRedirect(f"/d/{form_id}/{r.id}/")
