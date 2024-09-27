from rest_framework import viewsets
from .models import Investigation
from .serializers import InvestigationSerializer

class InvestigationViewSet(viewsets.ModelViewSet):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer

    def perform_create(self, serializer):
        # 여기서는 위경도와 관련된 데이터는 프론트에서 처리하므로, 자동으로 날짜는 저장
        serializer.save()