from django.contrib import admin
from .models import Coastline

@admin.register(Coastline)
class CoastlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias_names')  # 해안 이름만 표시
    search_fields = ['name', 'alias_names']  # 해안 이름으로 검색 가능