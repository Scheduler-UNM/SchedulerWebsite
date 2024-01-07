from django.db import models

class employee(models.Model):
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 32)
    email = models.CharField(max_length = 64)
    unmid = models.IntegerField()
    
    #shifts = models.ManyToManyField('common.Shift', related_name='employee')
    # ... other fields ...

    def __str__(self):
         return f'Name: {self.name}, Email: {self.email}'
