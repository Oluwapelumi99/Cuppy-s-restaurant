from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('booking/update_booking/<str:pk>/', views.update_booking, name='update_booking'),
    path('booking/cancel_booking/<str:pk>/', views.cancel_booking, name='cancel_booking'),
    path('booking/customer_bookings/', views.customer_bookings, name='customer_bookings')
]