from datetime import datetime

import africastalking
import requests
from django.conf import settings
from apps.customers.models import Customer
from apps.orders.models import Order

# Initialize SDK
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def send_sms(user, message, recipients):
    """
    Send sms
    """
    recipients = recipients
    message = message
    time_sent = datetime.now()
    

    try:
        response = sms.send(message, recipients)
        print(response)
        return response

    except Exception as e:
        print(f"Error sending sms: {e}")
        return None


def send_order_sms(order: Order):
    """
    Send sms to user after order is created
    """
    customer = order.customer
    message = f"Hello {customer.first_name}, your order has been received. Your order number is {order.order_id}. We will notify you once your order is ready for pick up."
    recipients = [customer.phone_number]
    send_sms(customer, message, recipients)