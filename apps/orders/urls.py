from django.urls import path
from .views import OrderList


app = 'apps.orders'

urlpatterns = [
    path('orders/', OrderList.as_view()),
    #path('orders/<int:pk>/', OrderViewSet.as_view()),
]
