from django.db import models
from account.models import Account
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey('account.Account',related_name='transactions', on_delete=models.CASCADE)
    transaction_id = models.AutoField(primary_key=True)
    transaction_choices = models.TextChoices('Inflow', 'Outflow')
    transaction_type = models.CharField(choices = transaction_choices.choices, max_length = 10)
    category = models.CharField(max_length = 264)
    description = models.CharField(max_length = 264)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    
