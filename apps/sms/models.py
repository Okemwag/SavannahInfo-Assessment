from django.db import models


class SmsInfo(models.Model):
    """
    general information about a group of SMS(s) is sent
    created per Africa'sTalking send SMS API call
    """
    success = models.BooleanField(
        default=False, editable=False, null=True)  
    message_text = models.CharField(
        max_length=160, editable=False, null=True)  
    africastalking_response = models.CharField(
        max_length=255, editable=False, null=True)  
    time_sent = models.DateTimeField(editable=False, null=True)
    time_added = models.DateTimeField(
        auto_now_add=True)  
    time_last_edited = models.DateTimeField(
        auto_now_add=True)
    #
    

    class Meta:
        ordering = ["time_last_edited"]

    def __str__(self):
        return f'Success: {self.success},  User: {self.user},  {self.time_added}  Response: {self.africastalking_response}'


class Message(models.Model):
    """
    information about a single SMS sent to a single receiver
    """
    
    message_id = models.CharField(max_length=255, editable=False)
    status_code = models.CharField(max_length=255, editable=False)
    cost = models.CharField(max_length=255, editable=False)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=255, null=True, blank=True, editable=False)
