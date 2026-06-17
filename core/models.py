from django.db import models

# ROUTE MODULE
class Route(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance_km = models.FloatField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origin} → {self.destination}"


# VEHICLE MODULE
class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('TRICYCLE', 'Tricycle'),
        ('VAN', 'Van'),
        ('BUS', 'Bus'),
    ]

    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default="Available")

    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type})"


# DRIVER MODULE
class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="Available")

    def __str__(self):
        return self.name


# ASSIGNMENT MODULE (CORE OF SYSTEM)
class Assignment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.driver} - {self.vehicle} - {self.route} ({self.status})"

class Alert(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    