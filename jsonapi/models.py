from django.db import models

# Create your models here.

class Accounts(models.Model):
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=5)
    balance = models.FloatField
    nature = models.CharField(max_length=50)
    transactions = models.IntegerField

class Transactions(models.Model):
    date = models.DateField
    description = models.CharField(max_length=200)
    amount = models.FloatField
    currency = models.CharField
    account_name = models.ForeignKey(Accounts, on_delete=models.CASCADE)


