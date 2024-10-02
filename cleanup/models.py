from django.db import models
from django.utils import timezone
import random

class Cleanup(models.Model):
    LITTER_CHOICES = [
        (1, 'Fishing Gear'),
        (2, 'Buoys'),
        (3, 'Household Waste'),
        (4, 'Large Illegal Dumping'),
        (5, 'Vegetation')
    ]

    # 청소자 이름 (프론트에서 숨김, 테스트 중 수동 입력)
    cleaner_name = models.CharField(max_length=255, blank=True) 

    # 청소 일련번호 (프론트에서 숨김, 자동 생성)
    cleanup_serial_number = models.CharField(max_length=20, unique=True, blank=True)

    # 해안명
    coast_name = models.CharField(max_length=255)
    
    # 해안길이
    coast_length = models.FloatField()

    # 청소 수거량 (사진, 마대개수)
    litter_bags_count = models.IntegerField()  # 50L 마대 개수
    collection_photo = models.ImageField(upload_to='photos/collection/', blank=True, null=True)  # 수거 사진

    # 수거량 환산 (마대개수 * 50L, 프론트에서 숨김)
    calculated_litter_amount = models.FloatField(editable=False, blank=True)

    # 일시 자동 입력
    timestamp = models.DateTimeField(default=timezone.now)

    # 위도 및 경도
    latitude = models.FloatField()
    longitude = models.FloatField()

    # 주요 쓰레기 선택
    main_litter_type = models.IntegerField(choices=LITTER_CHOICES)

    # 청소 완료 (전경 사진, 집하 장소 사진)
    completion_photo_landscape = models.ImageField(upload_to='photos/completion/landscape/', blank=True, null=True)
    completion_photo_collection_site = models.ImageField(upload_to='photos/completion/site/', blank=True, null=True)
    
    is_collected = models.BooleanField(default=False)  # 운전자가 수거 했는지 여부 확인 기본값 False

    def generate_serial_number(self):
        # 현재 날짜와 시간 + 3자리 무작위 숫자 조합으로 일련번호 생성
        current_time = timezone.now().strftime("%Y%m%d%H%M")
        random_number = str(random.randint(100, 999))
        return f"{current_time}{random_number}"

    def save(self, *args, **kwargs):
        # 일련번호가 비어 있을 때 자동 생성
        if not self.cleanup_serial_number:
            self.cleanup_serial_number = self.generate_serial_number()

        # 수거량 환산 (마대개수 * 50L)
        self.calculated_litter_amount = self.litter_bags_count * 50

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.coast_name} - {self.cleaner_name}"