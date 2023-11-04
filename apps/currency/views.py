from rest_framework import viewsets

from apps.currency.filters import CurrencyFilterSet
from apps.currency.models import Currency
from apps.currency.serializers import CurrencyRetrieveSerializer, CurrencyCreateSerializer, CurrencyListSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing currency instances.
    """
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()
    filterset_class = CurrencyFilterSet

    def get_serializers(self):
        serializers = {
            'retrieve': CurrencyRetrieveSerializer,
            'create': CurrencyCreateSerializer
        }
        return serializers

    def get_serializer_class(self):
        serializers = {**self.get_serializers()}
        if self.action in serializers:
            if serializer := serializers[self.action]:
                return serializer
        return self.serializer_class
