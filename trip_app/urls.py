from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('dashboard/', journeys_list, name='journeys-list')
]