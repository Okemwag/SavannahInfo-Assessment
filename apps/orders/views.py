from rest_framework import permissions, generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response
#from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope



# Create your views here.
class OrderList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except Order.DoesNotExist:
            raise APIException('No orders found')

    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        except Order.DoesNotExist:
            raise APIException('No orders found')
    

