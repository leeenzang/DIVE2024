from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coastline
from django.db.models import Q
from .serializers import CoastlineSerializer

# 해안선을 검색하는 API 뷰
@api_view(['GET'])
def search_coastlines(request):
    query = request.GET.get('q', '')  # 쿼리 파라미터에서 검색어를 가져옴

    # 이름 또는 별칭(alias_names)으로 검색
    coastlines = Coastline.objects.filter(
        Q(name__icontains=query) | Q(alias_names__icontains=query)
    )

    # 검색된 해안선들을 직렬화하여 응답으로 반환
    serializer = CoastlineSerializer(coastlines, many=True)
    return Response(serializer.data)