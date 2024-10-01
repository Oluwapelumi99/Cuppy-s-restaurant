from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('booking/cancel/<pk>/', views.cancelBooking.as_view(),name='cancel_booking'),
]