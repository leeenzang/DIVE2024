from django.http import JsonResponse
from django.db.models import Q
from investigation.models import Investigation
from cleanup.models import Cleanup
from common.models import Coastline

def filter_data_by_period_and_type(data_type, start_date, end_date, coast_names=None):
    if data_type == 'investigator':
        # 조사자 데이터를 기간으로만 필터링하거나 해안명을 추가로 필터링
        if coast_names:
            return Investigation.objects.filter(
                coast_name__in=coast_names,
                timestamp__range=(start_date, end_date)
            )
        else:
            return Investigation.objects.filter(timestamp__range=(start_date, end_date))
    elif data_type == 'cleanup':
        # 청소자 데이터를 기간으로만 필터링하거나 해안명을 추가로 필터링
        if coast_names:
            return Cleanup.objects.filter(
                coast_name__in=coast_names,
                timestamp__range=(start_date, end_date)
            )
        else:
            return Cleanup.objects.filter(timestamp__range=(start_date, end_date))
    return None

def filter_data(request):
    # GET 요청에서 기간과 데이터 유형, 지역 입력받음
    region_name = request.GET.get('region_name')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    data_type = request.GET.get('data_type')  # 조사자 또는 청소자 데이터 유형

    if not start_date or not end_date or not data_type or not region_name:
        return JsonResponse({'error': 'start_date, end_date, data_type, and region_name are required.'}, status=400)

    try:
        coast_names = None
        # 지역이 전체보기가 아닌 경우에만 해안명 필터링을 적용
        if region_name != '전체보기':
            # Coastline에서 large_area가 region_name과 일치하는 레코드 찾기
            coastlines = Coastline.objects.filter(large_area=region_name)
            
            if not coastlines.exists():
                return JsonResponse({'error': 'No matching coastlines found.'}, status=404)
            
            # Coastline 모델에서 name과 alias_names를 사용하여 coast_name 필터링 값 생성
            coast_names = []
            for coastline in coastlines:
                # name 추가
                coast_names.append(coastline.name)
                # alias_names가 있을 경우, ','로 구분된 각 값을 추가
                if coastline.alias_names:
                    coast_names.extend(coastline.alias_names.split(','))

        # 데이터 필터링 함수 호출 (전체보기인 경우 coast_names가 None)
        filtered_data = filter_data_by_period_and_type(data_type, start_date, end_date, coast_names)
        
        if filtered_data is None:
            return JsonResponse({'error': 'Invalid data type. Must be "investigator" or "cleanup".'}, status=400)

        # 필터링된 데이터가 없을 때
        if not filtered_data.exists():
            return JsonResponse({'message': 'No data found for the given period, data type, and region.'})

        # 필터링된 데이터를 JSON으로 반환 (조사자 또는 청소자에 따라 다른 필드)
        data_response = []
        if data_type == 'investigator':
            for data in filtered_data:
                data_response.append({
                    'coast_name': data.coast_name,
                    'latitude': data.latitude,
                    'longitude': data.longitude,
                    'estimated_litter_amount': data.estimated_litter_amount,
                    'main_litter_type': data.main_litter_type
                })
        elif data_type == 'cleanup':
            for data in filtered_data:
                data_response.append({
                    'coast_name': data.coast_name,
                    'latitude': data.latitude,
                    'longitude': data.longitude,
                    'calculated_litter_amount': data.calculated_litter_amount,
                    'main_litter_type': data.main_litter_type
                })

        return JsonResponse({'filtered_data': data_response})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)