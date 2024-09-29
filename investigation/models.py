from django.db import models
from django.utils import timezone
import random

class Investigation(models.Model):
    LITTER_CHOICES = [
        (1, 'Fishing Gear'),
        (2, 'Buoys'),
        (3, 'Household Waste'),
        (4, 'Large Illegal Dumping'),
        (5, 'Vegetation')
    ]
    
    investigator_name = models.CharField(max_length=255)  # 조사자 이름 수동 입력
    investigation_serial_number = models.CharField(max_length=20, unique=True, blank=True)  # 일련번호 자동 생성
    coast_name = models.CharField(max_length=255)
    coast_length = models.FloatField()  # 해안길이
    timestamp = models.DateTimeField(default=timezone.now)  # 일시 자동 입력
    latitude = models.FloatField()  # 위도
    longitude = models.FloatField()  # 경도
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  # 사진 저장 경로
    estimated_litter_amount = models.FloatField()  # 수거 예측량
    main_litter_type = models.IntegerField(choices=LITTER_CHOICES)  # 주요 쓰레기

    def generate_serial_number(self):
        # 현재 날짜와 시간 + 랜덤 숫자 조합으로 일련번호 생성
        current_time = timezone.now().strftime("%Y%m%d%H%M%S")
        random_number = str(random.randint(100, 999))
        return f"{current_time}{random_number}"

    def save(self, *args, **kwargs):
        # 일련번호가 비어 있을 때 자동 생성
        if not self.investigation_serial_number:
            self.investigation_serial_number = self.generate_serial_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.coast_name}"