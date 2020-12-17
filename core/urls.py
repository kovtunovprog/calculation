from django.urls import path
from .views import index, api_view

urlpatterns = [
    path('', index, name='index'),
    path('api/1.0/nums', api_view, name='api')
]