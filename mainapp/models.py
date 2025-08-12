from django.db import models
from django.contrib.auth.models import User

class HelpRequest(models.Model):
    seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='helprequests')  # Related name वापरल्यामुळे user.helprequests.all() मिळेल
    help_type = models.CharField(max_length=255)
    description = models.TextField()
    area = models.CharField(max_length=100)
    is_accepted = models.BooleanField(default=False)
    accepted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_helpers')  # Helper साठी related_name
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.help_type} - {self.area}"
