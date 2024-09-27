from django.db import models
from django.utils import timezone

class Cleanup(models.Model):
    LITTER_CHOICES = [
        (1, 'Fishing Gear'),
        (2, 'Buoys'),
        (3, 'Household Waste'),
        (4, 'Large Illegal Dumping'),
        (5, 'Vegetation')
    ]

    # 현장 도착 후 사진 촬영 (일시 및 위치 자동 입력)
    arrival_photo = models.ImageField(upload_to='photos/arrival/', blank=True)  # 사진 저장 경로 설정
    arrival_timestamp = models.DateTimeField(default=timezone.now)  # 도착 시 일시 자동 입력
    arrival_latitude = models.FloatField()  # 도착 위치 위도
    arrival_longitude = models.FloatField()  # 도착 위치 경도

    # 현장 상황 파악 후 입력 기능
    coast_name = models.CharField(max_length=255)
    coast_length = models.FloatField()  # 해안길이 (단위는 미터)

    # 쓰레기 수거량 (50L 마대 개수)
    litter_bags_count = models.IntegerField()  # 50L 마대 개수

    # 주요 쓰레기 선택
    main_litter_type = models.IntegerField(choices=LITTER_CHOICES)  # 주요 쓰레기 유형

    # 청소 완료 후 해안 및 집하 사진 업로드
    completion_photo_coast = models.ImageField(upload_to='photos/completion/coast/', blank=True)
    completion_photo_collection = models.ImageField(upload_to='photos/completion/collection/', blank=True)

    def __str__(self):
        return self.coast_name