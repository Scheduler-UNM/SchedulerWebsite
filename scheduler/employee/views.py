from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import employee, Access

def add_employee(request):
    if request.method == 'POST':
        # Extract data from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        unmid = request.POST['unmid']
        phonenumber = request.POST['phonenumber']
        access_ids = request.POST.getlist('access')  # This will be a list of Access IDs

        # Create a new employee instance
        new_employee = employee(
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
            unmid=unmid,
            phonenumber=phonenumber,
        )
        new_employee.save()  # Save the employee to generate an ID

        # Set the access values
        for access_id in access_ids:
            access_choices = Access.objects.all()
            print(access_choices)
            return render(request, 'employee/create_employee.html', {'access_choices': access_choices})

        # Redirect to a success page or show a success message
        return HttpResponse("Employee added successfully")
    else:
        # If not a POST request, just render the form
        # Fetch all Access objects to pass to the template
        access_choices = Access.objects.all()
        return render(request, 'employee/create_employee.html', {'access_choices': access_choices})

