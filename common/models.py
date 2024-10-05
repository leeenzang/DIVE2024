from django.db import models

class Coastline(models.Model):
    name = models.CharField(max_length=255)  # 해안 이름
    alias_names = models.TextField(blank=True, null=True)  # 해안의 별칭들을 쉼표로 구분하여 저장
    def __str__(self):
        return self.name