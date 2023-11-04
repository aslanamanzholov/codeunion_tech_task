import django_filters

from apps.currency.models import Currency


class CurrencyFilterSet(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=(
            ("name", "name"),
        )
    )

    class Meta:
        model = Currency
        fields = (
            'name',
        )
