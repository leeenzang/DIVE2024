from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestigationViewSet

router = DefaultRouter()
router.register(r'', InvestigationViewSet)  # 빈 문자열로 등록하면 기본 경로로 모든 CRUD 지원

urlpatterns = [
    path('', include(router.urls)),
]