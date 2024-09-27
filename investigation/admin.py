from django.contrib import admin
from .models import Investigation

# Investigation 모델을 Django Admin에 등록
@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
    # 관리자 페이지에 표시할 필드
    list_display = ('coast_name', 'coast_length_m', 'timestamp', 'latitude', 'longitude', 'estimated_litter_amount_L', 'main_litter_type')
    
    # 검색 필드 설정
    search_fields = ('coast_name', 'main_litter_type')
    
    # 필터 기능 추가
    list_filter = ('main_litter_type', 'timestamp')

    # 날짜와 위경도는 읽기 전용
    readonly_fields = ('timestamp', 'latitude', 'longitude')

    # 커스텀 메소드로 단위 표시
    def coast_length_m(self, obj):
        return f"{obj.coast_length} m"
    coast_length_m.short_description = 'Coast Length (m)'

    def estimated_litter_amount_L(self, obj):
        return f"{obj.estimated_litter_amount} L"
    estimated_litter_amount_L.short_description = 'Estimated Litter Amount (L)'