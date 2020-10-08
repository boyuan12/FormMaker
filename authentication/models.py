from django.db import models
import uuid

# Create your models here.
class Token(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_id = models.IntegerField()
    type = models.IntegerField() # 0: Verification, 1: Forgot Password
