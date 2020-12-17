from django.urls import path
from .views import index, calculate, api_view

urlpatterns = [
    path('', index, name='index'),
    path('api/1.0/nums/calculate', calculate, name='calculate'),
    path('api/1.0/nums', api_view, name='api')
]