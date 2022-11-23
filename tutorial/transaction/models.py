from django.db import models
from account.models import Account
# Create your models here.
# transaction_choices = models.TextChoices("Inflow", "Outflow")

transaction_choices = ((1,"Inflow"),(2, "Outflow"))

class Transaction(models.Model):
    account = models.ForeignKey(Account, related_name='account_transactions', on_delete=models.CASCADE)
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.IntegerField(choices=transaction_choices)
    category = models.CharField(max_length = 264)
    description = models.CharField(max_length = 264)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    
