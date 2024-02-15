from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.customers.urls')),
    path('api/', include('apps.orders.urls')),
    #path('api/', include('apps.sms')), 
]
