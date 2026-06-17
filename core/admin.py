from django.contrib import admin
from .models import Route, Vehicle, Driver, Assignment, Alert


#register your models here 


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'distance_km', 'fare')
    search_fields = ('origin', 'destination')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'vehicle_type', 'capacity', 'status')
    list_filter = ('vehicle_type', 'status')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'contact_number', 'status')
    search_fields = ('name',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('driver', 'vehicle', 'route', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('driver__name', 'vehicle__vehicle_number')
@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)