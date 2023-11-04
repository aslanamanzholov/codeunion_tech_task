import uuid

from django.core.management.base import BaseCommand

from apps.currency.models import Currency


class Command(BaseCommand):
    help = 'Список существующих валют к KZT'

    def add_arguments(self, parser):
        parser.add_argument('uuid', type=str, help='UUID Валюты')
        parser.add_argument('currency_name', type=str, help='Название валюты')
        parser.add_argument('currency_rate', type=str, help='Rate валюты')

    def handle(self, *args, **options):
        currency_uuid = options['uuid']
        currency_name = options['currency_name']
        currency_rate = options['currency_rate']
        currency = Currency.objects.get(uuid=currency_uuid)

        currency.name = currency_name
        currency.rate = currency_rate

        currency.save(update_fields=['name', 'rate'])

        self.stdout.write(self.style.SUCCESS(f'Валюта с ID {currency.uuid} была успешно обновлена.'))
        self.stdout.write(self.style.SUCCESS('Команда успешно выполнена!'))
