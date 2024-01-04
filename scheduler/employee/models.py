from django.db import models
from django.apps import apps
from django.utils import timezone
import datetime
    

class employee(models.Model):
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 32)
    email = models.CharField(max_length = 64)
    #shifts = models.ManyToManyField('common.Shift', related_name='employee')
    # ... other fields ...

    def __str__(self):
         return f'Name: {self.name}, Email: {self.email}'
    

    # def assign_shifts(self, shift_ids):
    #     # Get available shifts from the provided IDs
    #     #Shift = apps.get_model('common', 'Shift')
    #     available_shifts = Shift.objects.filter(id__in=shift_ids, assigned_employee__isnull=True)

    #     # Assign available shifts to this employee
    #     for shift in available_shifts:
    #         shift.assigned_employee = self.user
    #         shift.save()

    #     # Add these shifts to the employee's ManyToMany field
    #     self.shifts.set(available_shifts)

    #     # Return the number of shifts successfully assigned
    #     return len(available_shifts)

    # def assign_test_shifts(self):
    #     # Define the test shift times
    #     shift_times = [
    #         (datetime.time(8, 0), datetime.time(11, 0)),  # 8am-11am
    #         (datetime.time(11, 0), datetime.time(14, 0)),  # 11am-2pm
    #     ]

    #     assigned_shifts = []
    #     for start_time, end_time in shift_times:
    #         # Use timezone-aware datetime objects
    #         start_datetime = timezone.make_aware(datetime.datetime.combine(timezone.now().date(), start_time))
    #         end_datetime = timezone.make_aware(datetime.datetime.combine(timezone.now().date(), end_time))

    #         # Create or get the shift
    #         shift, created = Shift.objects.get_or_create(
    #             start_time=start_datetime,
    #             end_time=end_datetime
    #         )
    #         assigned_shifts.append(shift)

    #     # Update the employee's shifts
    #     self.shifts.set(assigned_shifts)

    #     return f"Assigned {len(assigned_shifts)} test shifts."
