from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser를 관리 페이지에 등록
admin.site.register(CustomUser, UserAdmin)