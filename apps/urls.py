from django.urls import include, path

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('currency/', include('apps.currency.urls')),
    path('users/', include('apps.users.urls')),
]
