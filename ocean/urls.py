from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('users/', include('users.urls')),  # users 앱의 URL을 포함
    path('investigation/', include('investigation.urls')),  # investigation 앱의 URL을 포함
    path('cleanup/', include('cleanup.urls')),  # cleanup 앱의 URL을 포함
    path('driver/', include('driver.urls')),  
    path('common/', include('common.urls')),  # common 앱의 URL 포함
    path('manager/', include('manager.urls')),  # common 앱의 URL 포함

    # Swagger URL
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]