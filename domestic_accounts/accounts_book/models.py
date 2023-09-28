from django.db import models

# Create your models here.
class RestAmount(models.Model):
    kind = models.CharField(max_length=30)
    rest_amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.kind)
    
class IncomePayment(models.Model):
    date = models.DateField()
    kind = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    income_or_payment = models.CharField(max_length=30)
    def __str__(self):
        return str(self.kind)