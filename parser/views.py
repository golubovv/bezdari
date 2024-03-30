from django.views.generic import ListView, DetailView, FormView
from django.http import JsonResponse

from .models import Event
from .parser import parser_iceShow, parser_kassy
from .forms import SearchEventForm

class EventsListView(ListView):
    template_name = 'parser/events.html'
    model = Event
    events = parser_iceShow()
    for event in events:
        if Event.objects.filter(**event) not in Event.objects.all():
            Event.objects.create(**event)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список событий'

        category = self.request.GET.get('category', None)
        if category != None:
            context['events'] = Event.objects.filter(category__slug=category)
        else:
            context['events'] = Event.objects.all()

        return context


class EventDetailView(DetailView):
    template_name = 'parser/detail_event.html'
    model = Event
    pk_url_kwarg = 'event_pk'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Событие'    #Потом сделаем динамическую генерацию с названием события

        return context
    

def search_events(request):
    search_by = request.GET.get('search_by', None)
    category = request.GET.get('category', None)
    print(category, 'AAAAAAAAAAAAAAAAAAAA')
    if search_by != None:
        events = Event.objects.filter(title__icontains=search_by, category__slug=category)
        print(1)
    else: 
        events = Event.objects.all()

    return JsonResponse(list(events.values()), safe=False)