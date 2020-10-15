from django.shortcuts import render
from form.models import Form, Response, ResponseQuestion, InputField

# Create your views here.
def view_submission(request, form_id, submission_id):
    # authenticate user to see if the user is the owner of the form
    form = Form.objects.get(id=form_id)
    # resp = Response.objects.get(id=submission_id)
    resp_qs = ResponseQuestion.objects.filter(response_id=submission_id)
    data = [] # [["label", "input"]]
    for r in resp_qs:
        i = InputField.objects.get(id=r.question_id)
        data.append([i.label, r.response])
    return render(request, "dashboard/view-response.html", {
        "data": data
    })

