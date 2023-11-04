from django.contrib import admin

from apps.currency.models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'rate')
    fields = ('uuid', 'name', 'rate')
    readonly_fields = ('uuid',)


# Register your models here.
admin.site.register(Currency, CurrencyAdmin)
