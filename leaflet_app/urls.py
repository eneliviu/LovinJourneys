from django.urls import path
from .views import (journey_list)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/',
         journey_list,
         name='journey-list'),
    path('dashboard/trip/create/',
         TripCreateView.as_view(),
         name='journey-create'),
    path('dashboard/trip/<int:pk>/',
         TripDetailView.as_view(),
         name='journey-detail'),
    path('dashboard/blog/<int:pk>/',
         BlogDetailView.as_view(),
         name='blog-detail'),
]