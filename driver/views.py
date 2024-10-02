# driver/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cleanup.models import Cleanup

@api_view(['GET'])
def uncollected_cleanup_view(request):
    # 수거되지 않은 데이터 필터링
    uncollected_data = Cleanup.objects.filter(is_collected=False)
    #응답 보낼 데이터
    data = uncollected_data.values('cleanup_serial_number', 'coast_name', 'latitude', 'longitude', 'litter_bags_count','calculated_litter_amount', 'main_litter_type', 'completion_photo_collection_site')

    return Response(data)


# driver/views.py (업데이트 함수 추가)
@api_view(['POST'])
def mark_as_collected(request, cleanup_id):
    try:
        cleanup = Cleanup.objects.get(cleanup_serial_number=cleanup_id)
        cleanup.is_collected = True
        cleanup.save()
        return Response({"message": "Cleanup marked as collected."}, status=200)
    except Cleanup.DoesNotExist:
        return Response({"error": "Cleanup not found."}, status=404)