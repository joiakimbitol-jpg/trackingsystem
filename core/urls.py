from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('routes/', views.route_list, name='routes'),
    path('fare/', views.fare_calculator, name='fare'),
    path('trips/', views.trips, name='trips'),
    path('alerts/', views.alerts, name='alerts'),
    path('trip/update/<int:id>/<str:status>/', views.update_trip_status, name='update_trip_status'),
    path('dispatch/', views.dispatch, name='dispatch'),
    path('reports/', views.reports, name='reports'),
    path('operator-dashboard/', views.operator_dashboard, name='operator_dashboard'),
    path('driver-dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('passenger-dashboard/', views.passenger_dashboard, name='passenger_dashboard'),
    path('login-redirect/', views.login_redirect, name='login_redirect'),
    path(
    'driver/start-trip/<int:id>/',
    views.driver_start_trip,
    name='driver_start_trip'
),
]