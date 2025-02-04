from django.urls import path
from .views import get_country_info

urlpatterns = [
    path('', get_country_info, name='country-info'),
]
