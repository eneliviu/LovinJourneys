from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  CreateView,
                                  DetailView)
from django.urls import reverse_lazy
from .models import Journey, Blog


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


class TripCreateView(CreateView):
    model = Journey
    success_url = reverse_lazy('journey-list')
    fields = ['place', 'country', 'start_date', 'end_date']
    # template model_form.html

    def form_valid(self, form):
        # make sure that owner field = logged user
        form.instance.tourist = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Journey

    # data stored on Journey must also have the Blog data
    def get_context_data(self, **kwargs):
        # current trip
        context = super().get_context_data(**kwargs)
        # add Blog data
        journey = context['object']
        context['blog'] = journey.blog.all()   # 'blog' is "related-name" in model
        return context


class BlogDetailView(DetailView):
    model = Blog