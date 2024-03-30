from django.urls import path
from parser import views

urlpatterns = [
    path('', 
         views.EventsListView.as_view(), name='main'),
    path('event/<int:event_pk>', 
         views.EventDetailView.as_view(), name='event_detail'),
     path('event/search', 
          views.search_events, name='search_events')
]