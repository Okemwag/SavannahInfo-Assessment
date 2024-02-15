from django.test import TestCase
from django.utils import timezone
from .models import SmsInfo, Message

class SmsInfoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a sample SmsInfo object for testing
        SmsInfo.objects.create(
            success=True,
            message_text='Test message',
            africastalking_response='Success',
            time_sent=timezone.now(),
            time_added=timezone.now(),
            time_last_edited=timezone.now()
        )

    def test_sms_info_str(self):
        sms_info = SmsInfo.objects.get(success=True)
        self.assertEqual(
            sms_info.__str__(),
            f'Success: True,  User: {sms_info.user},  {sms_info.time_added}  Response: Success'
        )

    def test_sms_info_default_success(self):
        # Check if the default value of success field is False
        sms_info = SmsInfo.objects.create()
        self.assertFalse(sms_info.success)

    # Add more tests as needed


class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a sample Message object for testing
        Message.objects.create(
            message_id='123456',
            status_code='200',
            cost='0.50',
            time_added=timezone.now(),
            time_last_edited=timezone.now()
        )

    def test_message_str(self):
        message = Message.objects.get(message_id='123456')
        self.assertEqual(
            message.__str__(),
            f'Message ID: {message.message_id}, Status Code: {message.status_code}, Cost: {message.cost}'
        )

    def test_message_blank_number(self):
        # Check if the number field can be blank
        message = Message.objects.create(
            message_id='789012',
            status_code='200',
            cost='0.50'
        )
        self.assertIsNone(message.number)

    # Add more tests as needed
