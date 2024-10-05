from django.contrib import admin
from .models import Coastline

@admin.register(Coastline)
class CoastlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias_names', 'large_area')  # large_area를 제거하고 기존 필드만 사용
    search_fields = ['name', 'alias_names', 'large_area']