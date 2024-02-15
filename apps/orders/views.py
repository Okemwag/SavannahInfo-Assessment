from rest_framework import permissions, generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response
#from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope



# Create your views here.
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)

