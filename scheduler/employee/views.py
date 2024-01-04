from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import employee


def index(request):
    # Assuming there's an employee profile with id=1
    profile = get_object_or_404(employee, id=1)
    return HttpResponse(str(profile))


def employee_details(request, employee_id):
    # Fetch the employee by ID or return 404 if not found
    employee_instance = get_object_or_404(employee, id=employee_id)

    # Fetch shifts related to the employee
    shifts = employee_instance.shifts.all()

    # Pass the employee and shifts to the template
    context = {
        'employee': employee_instance,
        'shifts': shifts,
    }

    return render(request, 'employee/employee_details.html', context)
