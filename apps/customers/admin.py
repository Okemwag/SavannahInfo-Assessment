from django.contrib import admin
from .models import Customer


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_created')
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['date_created']


admin.site.register(Customer, CustomerAdmin)