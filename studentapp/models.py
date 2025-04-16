from django.db import models

# Create your models here.

class feepayment(models.Model):
    stid =models.CharField(max_length=15)
    name =models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)



    def __str__(self):
        return f'{self.name}--{self.purpose}'



