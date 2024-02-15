from django.db import models
from apps.customers.models import Customer

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=200, unique=True)
    item = models.CharField(max_length=200)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
