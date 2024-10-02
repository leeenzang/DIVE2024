# driver/admin.py
from django.contrib import admin
from .models import DriverTask

@admin.register(DriverTask)
class DriverTaskAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'collection_date', 'task_end_time', 'total_collected_litter')
    search_fields = ('driver_name',)
    list_filter = ('collection_date',)

    # 읽기 전용 필드 (자동으로 입력된 필드)
    readonly_fields = ('collection_date', 'task_end_time', 'total_collected_litter', 'collected_serial_numbers')