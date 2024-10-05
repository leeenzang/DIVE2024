from django.urls import path
from .views import filter_data

urlpatterns = [
    path('filter-data/', filter_data, name='filter_data'),
]