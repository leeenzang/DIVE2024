# driver/urls.py
from django.urls import path
from .views import uncollected_cleanup_view, mark_as_collected, filter_selected_cleanup_view, mark_as_collected_driver

urlpatterns = [
    path('uncollected-cleanup/', uncollected_cleanup_view, name='uncollected-cleanup'),
    path('mark-as-collected/<int:cleanup_id>/', mark_as_collected, name='mark-as-collected'),
    path('filter-selected/', filter_selected_cleanup_view, name='filter-selected-cleanup'),
    path('mark-as-collected/<str:driver_name>/', mark_as_collected_driver, name='mark-as-collected-driver'),

]