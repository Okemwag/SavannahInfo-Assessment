from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    customer_id = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=False, unique=True)
    phone_number = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
