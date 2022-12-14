import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Account(models.Model):
    account_uuid = models.UUIDField("UUID", default=uuid.uuid4, editable=False)
    account_id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(User,related_name='accounts', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    #balance = models.PositiveIntegerField()

    def __str__(self):
        return  self.name
