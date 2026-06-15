from django.shortcuts import render
from .models import Driver, Vehicle, Route, Assignment

# DASHBOARD VIEW
def dashboard(request):
    total_drivers = Driver.objects.count()
    total_vehicles = Vehicle.objects.count()
    total_routes = Route.objects.count()
    active_assignments = Assignment.objects.filter(status='ACTIVE').count()

    context = {
        'total_drivers': total_drivers,
        'total_vehicles': total_vehicles,
        'total_routes': total_routes,
        'active_assignments': active_assignments,
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


def trips(request):
    trips = Assignment.objects.all()

    return render(request, 'core/trips.html', {
        'trips': trips
    })