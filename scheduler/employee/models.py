from django.db import models
from django.apps import apps
from django.utils import timezone
import datetime
    

class employee(models.Model):
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 32)
    email = models.CharField(max_length = 64)
    unmid = models.IntegerField(default=1)
    phonenumber = models.IntegerField(default=0000000000)
    
    ACCESS_CHOICES = [
        ('Administrator', 'Administrator'),
        ('Staff', 'Staff'),
        ('Student', 'Student'),
        ('Supervisor', 'Supervisor'),
    ]
    access = models.CharField(max_length=15, choices=ACCESS_CHOICES, default='Student')
    
    #shifts = models.ManyToManyField('common.Shift', related_name='employee')

    def __str__(self):
         return f'Name: {self.name}, Email: {self.email}'
    
