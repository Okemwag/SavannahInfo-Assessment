from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer')
    search_fields = ['order_id', 'customer']
    


admin.site.register(Order, OrderAdmin)
