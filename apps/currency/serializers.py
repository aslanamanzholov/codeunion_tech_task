from rest_framework import serializers

from apps.currency.models import Currency


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('uuid', 'name', 'rate')


class CurrencyRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('uuid', 'name', 'rate')


class CurrencyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('uuid', 'name', 'rate')
