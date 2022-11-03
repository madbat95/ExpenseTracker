from django.db import models
from user.models import User

# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key = True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
