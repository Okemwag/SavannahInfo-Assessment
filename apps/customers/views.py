from rest_framework import permissions, generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response


from .models import Customer
from .serializers import CustomerSerializer


class CustomerView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            raise APIException('No customers found')

    def post(self, request):
        try:
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        except Customer.DoesNotExist:
            raise APIException('No customers found')
