from django.db import models

# Create your models here.
class InputField(models.Model):
    label = models.CharField(max_length=100)
    form_id = models.IntegerField()

class Form(models.Model):
    name = models.CharField(max_length=100)
