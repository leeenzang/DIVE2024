from django.contrib import admin
from .models import Cleanup

@admin.register(Cleanup)
class CleanupAdmin(admin.ModelAdmin):
    list_display = ('id', 'coast_name', 'coast_length', 'litter_bags_count', 'main_litter_type', 'cleaner_name', 'cleanup_serial_number', 'is_collected')
    search_fields = ('coast_name', 'main_litter_type', 'cleaner_name')
    list_filter = ('main_litter_type', 'cleaner_name')

    # 실제로 모델에 존재하는 필드를 읽기 전용으로 설정
    readonly_fields = ('cleanup_serial_number', 'calculated_litter_amount', 'timestamp')