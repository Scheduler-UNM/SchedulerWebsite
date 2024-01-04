from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Pod, Shift
from django.contrib import messages

@require_http_methods(["GET", "POST"])
def create_pod(request):
    if request.method == "POST":
        # Extract data from the form
        name = request.POST.get('name')
        building = request.POST.get('building')
        building_info = request.POST.get('building_info')
        pod_supervisor = request.POST.get('pod_supervisor')
        is_shift_available = request.Post.get('is_shift_available')

        # Create and save the new Pod object
        new_pod = Pod(name=name, building=building, building_info=building_info, pod_supervisor=pod_supervisor)
        new_pod.save()

        messages.success(request, 'Pod was successfully added.')

        # Redirect back to the same page
        return redirect('create-pod')

    # Render the form template if request.method is not POST
    return render(request, 'common/create_pod.html')

@require_http_methods(["GET", "POST"])
def create_shift(request):
    if request.method == "POST":
        # Extract data from the form
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        pod_id = request.POST.get('pod')
        is_shift_available = request.POST.get('is_shift_available', 'on') == 'on'

        # Find the selected pod
        try:
            pod = Pod.objects.get(id=pod_id)
        except Pod.DoesNotExist:
            messages.error(request, 'Selected pod does not exist.')
            return redirect('create_shift')

        # Create and save the new Shift object
        new_shift = Shift(
            day=day,
            start_time=start_time,
            end_time=end_time,
            pod=pod,
            is_shift_available=is_shift_available,
        )
        new_shift.save()

        # Add a success message
        messages.success(request, 'Shift was successfully added.')

        # Redirect back to the form page
        return redirect('create_shift')

    # If request.method is GET or any other method, render the form page
    pods = Pod.objects.all()  # Fetch all pods to display in the form dropdown
    return render(request, 'common/create_shift.html', {'pods': pods})


