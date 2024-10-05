from django.db import models

class Coastline(models.Model):
    name = models.CharField(max_length=255)  # 해안 이름
    alias_names = models.CharField(max_length=255, blank=True, null=True)  # 별칭
    large_area = models.CharField(max_length=255, blank=True, null=True)  # 큰 지역

    def __str__(self):
        return self.name