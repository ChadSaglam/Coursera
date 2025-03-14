import datetime

from django.contrib.auth.models import User
from django.db import models


class CalendarSlot(models.Model):
    """Stores the calendar slots available for the user to book by other people.
    """
    belongs_to = models.ForeignKey(to=User, related_name='created_slots', on_delete=models.CASCADE, help_text="")
    created_at = models.DateTimeField(auto_now_add=True, help_text="")
    start_time = models.DateTimeField(help_text="")
    end_time = models.DateTimeField(help_text="")

    class Meta:
        ordering = ['-created_at']


class SlotBooking(models.Model):
    """Contains the booking details of the slots.
    """
    slot = models.OneToOneField(to=CalendarSlot, related_name='booking_details', on_delete=models.CASCADE, help_text="")
    booked_by = models.ForeignKey(to=User, related_name='booked_slots', on_delete=models.CASCADE, null=True, help_text="")
    booked_at = models.DateTimeField(auto_now_add=True, help_text="")
    description = models.TextField(null=True, help_text="")

    class Meta:
        ordering = ['-booked_at']