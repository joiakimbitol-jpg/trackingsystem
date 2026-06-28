from django.contrib.auth.decorators import login_required
from urllib import request
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver, Vehicle, Route, Assignment, Alert

# DASHBOARD VIEW
@login_required
def dashboard(request):
    if not (
    request.user.groups.filter(name='Admin').exists()
    or request.user.groups.filter(name='Operator').exists()
):
        return HttpResponse("Access Denied")
    total_drivers = Driver.objects.count()
    total_vehicles = Vehicle.objects.count()
    total_routes = Route.objects.count()
    active_assignments = Assignment.objects.filter(status='ACTIVE').count()
    latest_alerts = Alert.objects.order_by('-created_at')[:5]

    active_trips = Assignment.objects.filter(status='ACTIVE').count()
    pending_trips = Assignment.objects.filter(status='PENDING').count()
    completed_trips = Assignment.objects.filter(status='COMPLETED').count()
    cancelled_trips = Assignment.objects.filter(status='CANCELLED').count()

    context = {
        'total_drivers': total_drivers,
        'total_vehicles': total_vehicles,
        'total_routes': total_routes,
        'active_assignments': active_assignments,
        'latest_alerts': latest_alerts,

        'active_trips': active_trips,
        'pending_trips': pending_trips,
        'completed_trips': completed_trips,
        'cancelled_trips': cancelled_trips,
    }

    return render(request, 'core/dashboard.html', context)


def route_list(request):
    routes = Route.objects.all()

    return render(request, 'core/routes.html', {
        'routes': routes
    })


def fare_calculator(request):
    routes = Route.objects.all()
    result = None

    if request.method == "POST":
        origin = request.POST.get("origin")
        destination = request.POST.get("destination")

        route = Route.objects.filter(
            origin=origin,
            destination=destination
        ).first()

        if route:
            result = route.fare
        else:
            result = "No route found"

    return render(request, 'core/fare.html', {
        'routes': routes,
        'result': result
    })


@login_required
def trips(request):
    if not (
    request.user.groups.filter(name='Admin').exists()
    or request.user.groups.filter(name='Operator').exists()
):
        return HttpResponse("Access Denied")
    trips = Assignment.objects.all()

    return render(request, 'core/trips.html', {
        'trips': trips
    })
def update_trip_status(request, id, status):
    trip = get_object_or_404(Assignment, id=id)

    trip.status = status
    trip.save()

    if status == 'COMPLETED':
        trip.driver.status = 'Available'
        trip.driver.save()

        trip.vehicle.status = 'Available'
        trip.vehicle.save()

    return redirect('trips')
def alerts(request):
    alerts = Alert.objects.order_by('-created_at')

    return render(request, 'core/alerts.html', {
        'alerts': alerts
    })
def dispatch(request):
    drivers = Driver.objects.filter(status='Available')
    vehicles = Vehicle.objects.filter(status='Available')
    routes = Route.objects.all()

    if request.method == 'POST':

        driver_id = request.POST.get('driver')
        vehicle_id = request.POST.get('vehicle')
        route_id = request.POST.get('route')

        if driver_id and vehicle_id and route_id:

            driver = Driver.objects.get(id=driver_id)
            vehicle = Vehicle.objects.get(id=vehicle_id)
            route = Route.objects.get(id=route_id)

            Assignment.objects.create(
                driver=driver,
                vehicle=vehicle,
                route=route,
                status='PENDING'
            )

            driver.status = "Busy"
            driver.save()

            vehicle.status = "Busy"
            vehicle.save()

        return redirect('trips')

    return render(request, 'core/dispatch.html', {
        'drivers': drivers,
        'vehicles': vehicles,
        'routes': routes,
    })
def reports(request):
    context = {
        'total_drivers': Driver.objects.count(),
        'total_vehicles': Vehicle.objects.count(),
        'total_routes': Route.objects.count(),
        'total_assignments': Assignment.objects.count(),
        'active_trips': Assignment.objects.filter(status='ACTIVE').count(),
        'completed_trips': Assignment.objects.filter(status='COMPLETED').count(),
        'cancelled_trips': Assignment.objects.filter(status='CANCELLED').count(),
    }

    return render(request, 'core/reports.html', context)