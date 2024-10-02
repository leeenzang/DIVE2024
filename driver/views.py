from rest_framework.decorators import api_view
from rest_framework.response import Response
from cleanup.models import Cleanup
from driver.models import DriverTask
from django.utils import timezone

# 수거되지 않은 쓰레기 데이터를 필터링해서 보내주는 뷰
@api_view(['GET'])
def uncollected_cleanup_view(request):
    # 수거되지 않은 데이터 필터링
    uncollected_data = Cleanup.objects.filter(is_collected=False)

    # 응답 데이터 구성
    data = uncollected_data.values(
        'cleanup_serial_number', 
        'coast_name', 
        'latitude', 
        'longitude', 
        'litter_bags_count',
        'calculated_litter_amount', 
        'main_litter_type', 
        'completion_photo_collection_site'
    )
    
    return Response(data)

# 수거 완료로 표시하는 함수 (cleanup_serial_number 사용)
@api_view(['POST'])
def mark_as_collected(request, cleanup_serial_number):
    try:
        cleanup = Cleanup.objects.get(cleanup_serial_number=cleanup_serial_number)
        cleanup.is_collected = True
        cleanup.save()
        return Response({"message": "Cleanup marked as collected."}, status=200)
    except Cleanup.DoesNotExist:
        return Response({"error": "Cleanup not found."}, status=404)

# 선택된 수거 데이터를 필터링해서 보내주는 뷰
@api_view(['POST'])
def filter_selected_cleanup_view(request):
    # 프론트엔드에서 전달된 선택된 cleanup_serial_number 리스트를 받음
    selected_serial_numbers = request.data.get('selected_serial_numbers', [])

    # 선택된 serial_number에 해당하는 수거 데이터를 필터링
    selected_cleanup_data = Cleanup.objects.filter(cleanup_serial_number__in=selected_serial_numbers)

    # 필요한 데이터만 응답으로 보내기
    data = selected_cleanup_data.values(
        'cleanup_serial_number', 
        'coast_name', 
        'latitude', 
        'longitude', 
        'main_litter_type',
        'litter_bags_count',
        'calculated_litter_amount',
        'completion_photo_collection_site',
    )

    return Response(data)
    
@api_view(['POST'])
def mark_as_collected_driver(request, driver_name):
    try:
        # 프론트엔드에서 전달된 청소자 일련번호 리스트
        collected_serial_numbers = request.data.get('collected_serial_numbers', [])
        
        # 청소자 데이터를 조회하여 총 수거량 계산
        total_collected_litter = 0
        for serial_number in collected_serial_numbers:
            cleanup = Cleanup.objects.get(cleanup_serial_number=serial_number)
            total_collected_litter += cleanup.calculated_litter_amount  # 이미 계산된 수거량을 더함

        # 운전자가 완료한 작업을 기록
        driver_task = DriverTask(
            driver_name=driver_name,
            total_collected_litter=total_collected_litter,  # 총 수거량 저장
            collected_serial_numbers=collected_serial_numbers
        )

        driver_task.save()

        return Response({"message": "Driver task marked as completed.", "total_collected_litter": total_collected_litter}, status=200)
    except Cleanup.DoesNotExist:
        return Response({"error": "Cleanup data not found."}, status=404)