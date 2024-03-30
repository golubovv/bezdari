from django.core.management.base import BaseCommand

from parser.parser import parser_iceShow, parser_kassy
from parser.models import Event


class Command(BaseCommand):
    help = 'Парсит все сайты и записывает новые результаты в бд'

    def handle(self, *args, **kwargs):
        events = parser_kassy() + parser_iceShow


