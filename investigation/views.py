from rest_framework import viewsets
from .models import Investigation
from .serializers import InvestigationSerializer

class InvestigationViewSet(viewsets.ModelViewSet):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer

    def perform_create(self, serializer):
        # 사용자 입력 기반으로 데이터를 저장
        serializer.save()