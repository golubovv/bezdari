from django.views.generic import ListView, DetailView

from .models import Event
from .parser import parser_iceShow

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