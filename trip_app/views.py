from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Journey


# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip_app/index.html'


def journey_list(request):
    print(Journey)
    print(request.user)
    
    journeys = Journey.objects.filter(tourist=request.user.id)
    context = {
        'journeys': journeys
    }
    return render(request,
                  'trip_app/journey_list.html',
                  context)
