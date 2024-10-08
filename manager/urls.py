from django.urls import path
from .views import (filter_data, 
    get_total_collection_trend,
    get_litter_type_ratio,
    get_predicted_vs_actual_comparison,
    CreateUserView,
    UserListView,
    DeleteUserView,
)
urlpatterns = [
    path('filter-data/', filter_data, name='filter_data'),
    path('total-collection-trend/', get_total_collection_trend, name='total_collection_trend'),
    path('litter-type-ratio/', get_litter_type_ratio, name='litter_type_ratio'),
    path('predicted-vs-actual-comparison/', get_predicted_vs_actual_comparison, name='predicted_vs_actual_comparison'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('users-list/', UserListView.as_view(), name='user-list'),  # 회원 목록 조회 엔드포인트
    path('users/<str:username>/delete/', DeleteUserView.as_view(), name='delete-user'),  # 회원 삭제 엔드포인트

]