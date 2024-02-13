from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=200, db)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
