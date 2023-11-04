from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.currency.views import CurrencyViewSet

router = DefaultRouter(trailing_slash=True)
router.register('', CurrencyViewSet, basename='currency')

urlpatterns = [
    path('', include(router.urls))
]
