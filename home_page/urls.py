from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path(
        'review/', views.review_list, name='review_list'),
    path(
        'submit_review/', views.submit_review, name='submit_review'),
    path(
        'review/edit_review/<str:pk>/', views.edit_review, name='edit_review'),
    path(
        'review/delete_review/<str:pk>/',
        views.delete_review, name='delete_review'),
]
