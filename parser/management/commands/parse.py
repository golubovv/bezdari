from django.core.management.base import BaseCommand

from parser.parser import parser_kassy
from parser.models import Event, Category


class Command(BaseCommand):
    help = 'Парсит все сайты и записывает новые результаты в бд'

    def handle(self, *args, **kwargs):
        events = parser_kassy()
        for event in events:
            event['category'] = Category.objects.get(slug='theater')
            Event.objects.create(**event)


