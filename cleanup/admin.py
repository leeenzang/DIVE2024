from django.contrib import admin
from .models import Cleanup

@admin.register(Cleanup)
class CleanupAdmin(admin.ModelAdmin):
    list_display = ('coast_name', 'coast_length', 'litter_bags_count', 'main_litter_type')
    search_fields = ('coast_name', 'main_litter_type')
    list_filter = ('main_litter_type',)

    readonly_fields = ('arrival_timestamp', 'arrival_latitude', 'arrival_longitude')  # 읽기 전용 필드 설정