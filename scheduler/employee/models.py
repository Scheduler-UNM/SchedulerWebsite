from django.db import models
from django.apps import apps
from django.utils import timezone
import datetime
    

class employee(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64,default='No Last Name')
    phonenumber = models.IntegerField(default=0000000000)
    email = models.CharField(max_length = 64)
    password = models.CharField(max_length = 32)
    unmid = models.IntegerField(default=1)
    phonenumber = models.IntegerField(default=0000000000)
    
    ACCESS_CHOICES = [
        ('Administrator', 'Administrator'),
        ('Staff', 'Staff'),
        ('Student', 'Student'),
        ('Supervisor', 'Supervisor'),
    ]
    access = models.ManyToManyField(
        'Access',  # Assuming 'Access' is a separate model that stores these roles.
        blank=True,
    )
    # supervisor = models.ForeignKey(
    #     'self',  # Refer to the same model.
    #     on_delete=models.SET_NULL,  # Define the behavior when a supervisor is deleted.
    #     null=True, 
    #     blank=True,  # Allow this field to be blank (not every employee might have a supervisor).
    #     limit_choices_to={'access': 'Administrator'},  # Limit choices to employees with Administrator access.
    #     related_name='supervisees'  # Allows reverse relation from supervisor to their supervisees.
    # )

    ##will need to add supervisor field, but the import cannot be circular, other way is to move employee model
    #common app. But deleting app can be directory. Please follow the official django documentation to delete
    #an employee app. 
    
    #shifts = models.ManyToManyField('common.Shift', related_name='employee')

    def __str__(self):
         return f'Name: {self.first_name} {self.last_name}, Email: {self.email}, Access: {self.access.name}'
    

class Access(models.Model):
    name = models.CharField(max_length=15, choices=employee.ACCESS_CHOICES)

    def __str__(self):
        return self.name
    
