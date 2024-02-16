from django.test import TestCase
from apps.customers.models import Customer
from .models import Order

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create(name='Test Customer')

    def setUp(self):
        
        self.order = Order.objects.create(
            customer=self.customer,
            order_id='TEST123',
            item='Test Item',
            amount=100,
        )

    def test_order_creation(self):
        """Test Order model creation"""
        self.assertIsInstance(self.order, Order)
        self.assertEqual(Order.objects.count(), 1)

    def test_order_fields(self):
        """Test Order model fields"""
        order = Order.objects.get(order_id='TEST123')
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.order_id, 'TEST123')
        self.assertEqual(order.item, 'Test Item')
        self.assertEqual(order.amount, 100)

    def test_order_str_representation(self):
        """Test Order model string representation"""
        self.assertEqual(str(self.order), 'Test Item')

    def test_order_time_auto_now_add(self):
        """Test Order model time field auto_now_add"""
        order = Order.objects.create(
            customer=self.customer,
            order_id='TEST456',
            item='Another Item',
            amount=200,
        )
        self.assertIsNotNone(order.time)

    def test_order_unique_order_id(self):
        """Test Order model unique order_id constraint"""
        with self.assertRaises(Exception):
            Order.objects.create(
                customer=self.customer,
                order_id='TEST123',  
                item='Another Item',
                amount=200,
            )
