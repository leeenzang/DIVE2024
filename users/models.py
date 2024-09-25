from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 사용자 역할 추가
    ROLE_CHOICES = (
        ('investigator', 'Investigator'),
        ('cleaner', 'Cleaner'),
        ('admin', 'Admin'),
        ('driver', 'Driver'),
    )
    
    # first_name, last_name 대신 name 필드 사용
    name = models.CharField(max_length=255)
    # 사용자 역할 필드 추가
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='investigator')

    # username을 로그인 ID로 사용
    USERNAME_FIELD = 'username'
    
    # 회원가입 시 필수 필드 (name, role만 필수로 설정)
    REQUIRED_FIELDS = ['name', 'role']

    def __str__(self):
        return self.username  # 출력할 때는 ID를 사용