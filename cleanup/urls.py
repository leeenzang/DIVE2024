from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CleanupViewSet

router = DefaultRouter()
router.register(r'', CleanupViewSet)

urlpatterns = [
    path('', include(router.urls)),  # 기본 경로로 모든 CRUD 작업 처리
]