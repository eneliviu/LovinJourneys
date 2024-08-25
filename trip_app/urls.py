from django.urls import path
from .views import HomeView, journey_list

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', journey_list, name='journey-list')
]