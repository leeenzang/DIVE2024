from django.db import models
from django.utils import timezone

class Investigation(models.Model):
    LITTER_CHOICES = [
        (1, 'Fishing Gear'),
        (2, 'Buoys'),
        (3, 'Household Waste'),
        (4, 'Large Illegal Dumping'),
        (5, 'Vegetation')
    ]
    
    coast_name = models.CharField(max_length=255)
    coast_length = models.FloatField()  # 해안길이 (단위는 미터로 생각)
    timestamp = models.DateTimeField(default=timezone.now)  # 일시 자동 입력
    latitude = models.FloatField()  # 위도 자동
    longitude = models.FloatField()  # 경도 자동
    photo = models.ImageField(upload_to='photos/', blank=True)  # 사진 저장 경로
    estimated_litter_amount = models.FloatField()  # 수거 예측량
    main_litter_type = models.IntegerField(choices=LITTER_CHOICES)  # 주요 쓰레기 (숫자로 매핑)

    def __str__(self):
        return self.coast_name