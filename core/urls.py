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
]