import uuid
from django.db import models
from account.models import Account
# Create your models here.
# transaction_choices = models.TextChoices("Inflow", "Outflow")

transaction_choices = (("Inflow","Inflow"),("Outflow", "Outflow"))

class Transaction(models.Model):
    transaction_uuid = models.UUIDField("UUID", default=uuid.uuid4, editable=False)
    source = models.ForeignKey(Account, related_name='account_source', on_delete=models.CASCADE)
    destination = models.ForeignKey(Account, related_name='account_destination', on_delete=models.CASCADE)
    transaction_id = models.AutoField(primary_key = True)
    transaction_type = models.CharField(max_length = 9, choices=transaction_choices)
    category = models.CharField(max_length = 264)
    description = models.CharField(max_length = 264)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.source.balance += self.amount
        self.source.save()
        super(Transaction, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.source.balance -= self.amount
        self.source.save()
        self.destination.balance += self.amount
        self.destination.save()
        super(Transaction, self).delete(*args, **kwargs) 
