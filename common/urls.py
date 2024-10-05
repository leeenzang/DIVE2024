from django.urls import path
from .views import search_coastlines

urlpatterns = [
    path('search/', search_coastlines, name='coastline_search'),
]