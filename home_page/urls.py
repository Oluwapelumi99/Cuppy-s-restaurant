from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home_page'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('edit_review/<str:pk>/', views.edit_review, name='edit_review'),
    path('delete_review/<str:pk>/', views.delete_review, name='delete_review')
]