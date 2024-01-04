from django.contrib import admin
from .models import Shift, ShiftRequest, Pod

# Register your models here.
admin.site.register(Pod)
admin.site.register(Shift)