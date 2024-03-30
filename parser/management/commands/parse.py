from django.core.management.base import BaseCommand

from parser.parser import parser_kassy, parser_kinopoisk
from parser.models import Event, Category


class Command(BaseCommand):
    help = 'Парсит все сайты и записывает новые результаты в бд'

    def handle(self, *args, **kwargs):
        Event.objects.all().delete()
        events = parser_kassy()
        for event in events:
            event['category'] = Category.objects.get(slug='theater')
            Event.objects.create(**event)
        
        events = parser_kinopoisk()
        for event in events:
            event['category'] = Category.objects.get(slug='cinema')
            Event.objects.create(**event)


