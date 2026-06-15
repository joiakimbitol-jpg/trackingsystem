from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('routes/', views.route_list, name='routes'),
    path('fare/', views.fare_calculator, name='fare'),
    path('trips/', views.trips, name='trips'),
]