from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# CustomUser 모델을 기반으로 회원가입 폼 작성
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'name', 'role']
        
        # role 필드를 드롭다운으로 표시할 수 있도록 위젯 설정
        widgets = {
            'role': forms.Select(choices=CustomUser.ROLE_CHOICES),
        }