from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home_page'),
    path('accounts/email/confirm/<key>/', views.CustomEmailConfirmationView, name = 'email_confirmation')
]