from django.urls import path
from .views import CustomerView


app = 'apps.customers'

urlpatterns = [
    path('customers/', CustomerView.as_view()),
]