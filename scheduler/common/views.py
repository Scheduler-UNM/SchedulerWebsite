# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Pod, Shift
from django.contrib import messages

@require_http_methods(["GET", "POST"])
def create_pod(request):
    if request.method == "POST":
        # Extract data from the form
        location_name = request.POST.get('location_name')
        full_location = request.POST.get('full_location')
        room_no = request.Post.get('room_no')
        building_info = request.POST.get('building_info')
        pod_supervisor = request.POST.get('pod_supervisor')


        # Create and save the new Pod object
        new_pod = Pod(location_name=location_name, full_location=full_location, building_info=building_info,room_no=room_no, pod_supervisor=pod_supervisor,active=True)
        new_pod.save()

        messages.success(request, 'Pod was successfully added.')

        # Redirect back to the same page
        return redirect('create-pod')

    # Render the form template if request.method is not POST
    return render(request, 'common/create_pod.html')

@require_http_methods(["GET", "POST"])
def create_shift(request):
    if request.method == "POST":
        start_date=request.Post.get('start_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        pod_id = request.POST.get('pod')
        shift_term = request.Post.get('shift_term')
        shift_slots = request.Post.get('shift_slots')
        shift_repeats = request.Post.get('shift_repeats')
        

        try:
            pod = Pod.objects.get(id=pod_id)
        except Pod.DoesNotExist:
            messages.error(request, 'Selected pod does not exist.')
            return redirect('create_shift')

        new_shift = Shift(
            day=day,
            start_time=start_time,
            end_time=end_time,
            pod=pod,
            is_available=is_available
        )
        new_shift.save()

        messages.success(request, 'Shift was successfully added.')
        return redirect('create_shift')

    else:
        pods = Pod.objects.all()
        return render(request, 'common/create_shift.html', {'pods': pods})


