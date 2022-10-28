# from django.db import models
# from django.contrib.auth.hashers import make_password

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length = 128, blank = False, default = '')
#     user_name = models.CharField(max_length=50,unique=True)
#     #password = make_password("plain_text")
#     email = models.EmailField(max_length=30, unique=True)
#     dob = models.DateField()


# class Account(models.Model):
#     account_id = models.AutoField(primary_key = True)
#     user_id = models.ForeignKey('User', on_delete=models.CASCADE)
#     name = models.CharField(max_length=128)


# class Transaction(models.Model):
#     account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
#     transaction_id = models.AutoField(primary_key=True)
#     transaction_choices = models.TextChoices('Inflow', 'Outflow')
#     transaction_type = models.CharField(choices = transaction_choices.choices, max_length = 10)
#     category = models.CharField(max_length = 264)
#     description = models.CharField(max_length = 264)
#     amount = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)


