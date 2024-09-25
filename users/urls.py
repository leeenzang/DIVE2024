from django.urls import path
from .views import SignUpView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # 회원가입 API URL
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # 로그인 API
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 갱신 API
]