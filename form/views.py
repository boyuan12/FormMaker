from django.shortcuts import redirect, render
from .models import Form, InputField, Response, ResponseQuestion, MultipleChoiceOption, MultipleChoiceField
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
@login_required(login_url='/auth/login/')
def create(request):
    if request.method == "POST":
        Form(name=request.POST["form-name"], user_id=request.user.id).save()
        f = Form.objects.filter(name=request.POST["form-name"])[::-1][0]
        print(json.loads(request.POST["muls"]))

        try:
            muls = json.loads(request.POST["muls"])
            for i in muls:
                # create a new MC question, with label request.POST[mul-i]
                label = request.POST["mul-" + i]
                MultipleChoiceField(label=label, form_id=f.id, order=i).save()
                m = MultipleChoiceField.objects.filter(label=label)[::-1][0]
                option_count = muls[i]
                for j in range(option_count + 1):
                    print(j)
                    # create option
                    op_label = f"mul-{i}-op-{j}"
                    MultipleChoiceOption(label=request.POST[op_label], question_id=m.id).save()
        except Exception as e:
            pass

        # Short Input
        for i in range(int(request.POST["questionCount"])):
            try:
                InputField(label=request.POST[str(i)], form_id=f.id, order=i).save()
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

    return render(request, "form/view-form.html", {
        "form_id": form_id,
        "questions": questions
    })


def submit_form(request, form_id):
    # print(request.POST)
    Response(user_id=request.user.id, form_id=form_id).save()
    r = Response.objects.filter(user_id=request.user.id, form_id=form_id)[::-1][0]
    for i in request.POST:
        if i == "csrfmiddlewaretoken":
            continue
        ResponseQuestion(question_id=i, response=request.POST[i], response_id=r.id).save()
    return HttpResponse("success")
