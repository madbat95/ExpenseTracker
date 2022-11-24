import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ["email", "dob"]
    name = models.CharField(max_length = 128, blank = False, default = '')
    dob = models.DateField()
    user_uuid = models.UUIDField("UUID", default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.name

