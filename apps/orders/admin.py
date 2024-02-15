from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'date_created', 'status')
    search_fields = ['order_id', 'customer']
    list_filter = ['date_created', 'status']


admin.site.register(Order, OrderAdmin)
