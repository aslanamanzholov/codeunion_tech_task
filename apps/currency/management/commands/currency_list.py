from django.core.management.base import BaseCommand

from apps.currency.models import Currency


class Command(BaseCommand):
    help = 'Список существующих валют к KZT'

    def handle(self, *args, **options):
        currency_list = Currency.objects.all().values('name', 'rate')

        for currency in currency_list:
            self.stdout.write(f'Название валюты: {currency["name"]}, Rate: {currency["rate"]}')

        self.stdout.write(self.style.SUCCESS('Команда успешно выполнена!'))
