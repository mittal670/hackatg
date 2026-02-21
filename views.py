from django.shortcuts import render, redirect
from .models import Trip
from .forms import TripForm
from fleet.models import Vehicle

def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.status = 'dispatched'
            trip.save()

            # Update Vehicle Status
            trip.vehicle.status = 'on_trip'
            trip.vehicle.save()

            return redirect('trip_list')
    else:
        form = TripForm()

    return render(request, 'trips/create_trip.html', {'form': form})


def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})