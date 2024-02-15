from django.test import TestCase
from .models import Customer
from django.utils import timezone

class CustomerModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            customer_id='123456',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone_number='1234567890'
        )

    def test_customer_creation(self):
        """Test customer model creation"""
        self.assertEqual(self.customer.customer_id, '123456')
        self.assertEqual(self.customer.first_name, 'John')
        self.assertEqual(self.customer.last_name, 'Doe')
        self.assertEqual(self.customer.email, 'john@example.com')
        self.assertEqual(self.customer.phone_number, '1234567890')
        self.assertTrue(isinstance(self.customer.date_created, timezone.datetime))
        self.assertIsNotNone(self.customer.date_created)

    def test_customer_str_representation(self):
        """Test customer __str__ method"""
        expected_str = f"{self.customer.first_name} {self.customer.last_name}"
        self.assertEqual(str(self.customer), expected_str)
