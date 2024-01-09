from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.conf import settings
from employee.models import employee
from datetime import date

class Terms(models.Model):
    name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return f'Term {self.name} begining from {self.start_date} and ending at {self.end_date}'


class Pod(models.Model):
    AVAILABLE_CHOICES = [
        (1, 'ACTIVE'),
        (2, 'INACTIVE'),
    ]
    location_name = models.CharField(max_length=32,default='NULL')
    full_location_name = models.CharField(max_length=100,default='NULL')
    building_info = models.IntegerField()
    room_no = models.IntegerField(default=1)
    pod_supervisor = models.CharField(max_length=64, default="null")
    active = models.IntegerField(choices=AVAILABLE_CHOICES, default=1)

    def __str__(self):
        return f'Pod {self.name} at Building{self.building} supervised by {self.pod_supervisor}'
    


class Shift(models.Model):
    DAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]
    AVAILABLE_CHOICES = [
        (1, 'Reserved'),
        (0, 'Unavailable'),
    ]
    # Basic shift details
    start_date=models.DateField(default=date(2000,1,1))
    start_time = models.TimeField()
    end_time = models.TimeField()
    pod = models.ForeignKey('Pod', on_delete=models.CASCADE, related_name='shifts', null=True)
    shift_repeats=models.BooleanField(default=True)
    shift_slots = models.IntegerField(default=16)
    reserved_by = models.ForeignKey(employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='reserved_shifts')
    shift_term = models.ForeignKey(Terms, on_delete=models.CASCADE, related_name='shifts', null=True)

    def is_shift_available(self):
        # Method to check if the shift is available for assignment
        return self.is_available

    # Additional methods for shift management can be added here

    def __str__(self):
        #return f'Shift at {self.pod} from {self.start_time} to {self.end_time}'
        return f'Shift on {self.day} in {self.pod.name} from {self.start_time} to {self.end_time} and is_available={self.is_available}'

class ShiftRequest(models.Model):
    # Types of requests
    SWAP = 'swap'
    COVERAGE = 'coverage'
    GIVEAWAY = 'giveaway'
    REQUEST_TYPES = [
        (SWAP, 'Swap'),
        (COVERAGE, 'Coverage'),
        (GIVEAWAY, 'Giveaway'),
    ]

    # Basic request details
    requesting_employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shift_requests')
    requested_shift = models.ForeignKey('Shift', on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPES)

    # Status of the request
    PENDING = 'pending'
    APPROVED = 'approved'
    DENIED = 'denied'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    # Timestamps for tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Method to approve request
    def approve(self):
        self.status = self.APPROVED
        self.save()

    # Method to deny request
    def deny(self):
        self.status = self.DENIED
        self.save()

    def __str__(self):
        return f'{self.request_type.title()} Request by {self.requesting_employee} for {self.requested_shift}'

    # Additional methods and logic can be added here

