from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 비밀번호는 응답에 포함되지 않도록 설정

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'name', 'role', 'contact']
    
    # 비밀번호는 암호화하여 저장하도록 처리
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            role=validated_data['role'],
            contact=validated_data['contact'] 
        )
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)  # 기본 인증 로직을 실행
        # 사용자 정보 추가
        data['username'] = self.user.username
        data['name'] = self.user.name
        data['role'] = self.user.role
        return data