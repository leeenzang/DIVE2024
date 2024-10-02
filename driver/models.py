from django.utils import timezone
from django.db import models
import random

class DriverTask(models.Model):
    driver_name = models.CharField(max_length=255)  # 운전자 이름 (수동 입력 또는 자동 설정)

    driver_task_serial_number = models.CharField(max_length=20, unique=True, blank=True)

    collection_date = models.DateField(default=timezone.now)  # 수거 완료 날짜 자동 입력
    task_end_time = models.TimeField(default=timezone.now)  # 작업 종료 시간 자동 입력

    total_collected_litter = models.FloatField(blank=True, null=True)

    collected_serial_numbers = models.JSONField(blank=True, null=True)

    def generate_serial_number(self):
        current_time = timezone.now().strftime("%Y%m%d%H%M%S")
        random_number = str(random.randint(100, 999))
        return f"{current_time}{random_number}"

    def save(self, *args, **kwargs):
        if not self.driver_task_serial_number:
            unique = False
            while not unique:
                serial_number = self.generate_serial_number()
                if not DriverTask.objects.filter(driver_task_serial_number=serial_number).exists():
                    self.driver_task_serial_number = serial_number
                    unique = True
                else:
                    print(f"Duplicate serial number generated: {serial_number}. Retrying...")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.driver_name} - {self.collection_date}"