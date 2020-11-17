from django.db import models
import uuid

# Create your models here.
class InputField(models.Model):
    order = models.IntegerField()
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    label = models.CharField(max_length=100)
    form_id = models.IntegerField()

class Form(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.IntegerField()

class Response(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_id = models.IntegerField()
    form_id = models.IntegerField()

class ResponseQuestion(models.Model):
    question_id = models.IntegerField()
    response = models.CharField(max_length=255)
    response_id = models.IntegerField()

class MultipleChoiceField(models.Model):
    order = models.IntegerField()
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    label = models.CharField(max_length=100)
    form_id = models.IntegerField()

class MultipleChoiceOption(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    label = models.CharField(max_length=100)
    question_id = models.IntegerField()
