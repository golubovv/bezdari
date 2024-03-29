from django.urls import path
from .views import EventsListView, EventDetailView

urlpatterns = [
    path('', 
         EventsListView.as_view(), name='main'),
    path('event/<int:event_pk>', 
         EventDetailView.as_view(), name='event_detail')
]