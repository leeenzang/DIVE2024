from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('users/', include('users.urls')),  # users 앱의 URL을 포함
    path('investigation/', include('investigation.urls')),  # investigation 앱의 URL을 포함
    path('cleanup/', include('cleanup.urls')),  # cleanup 앱의 URL을 포함
]