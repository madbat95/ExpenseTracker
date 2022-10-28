from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import DateField


class User(AbstractUser):
    name = models.CharField(max_length = 128, blank = False, default = '')
    dob = models.DateField()

    pass


