import os
import django
import pandas as pd

# Django 설정 파일 경로 지정 (settings.py가 위치한 경로)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ocean.settings')
django.setup()

# Django 모델 가져오기
from cleanup.models import Cleanup

# 엑셀 파일 읽기 (파일 경로 수정)
excel_file_path = '/Users/ieunjin/Downloads/cleanup.xlsx'
df = pd.read_excel(excel_file_path)

# 각 행을 Django 모델로 변환하여 저장
for index, row in df.iterrows():
    cleanup = Cleanup(
        # 청소자 성명
        cleaner_name=row['청소자 성명'],

        # 청소 일련번호 (엑셀 데이터에 있지만, 자동 생성이 필요하다면 이 값을 무시할 수도 있음)
        cleanup_serial_number=row['청소 일련번호'],

        # 청소 시기 (엑셀 데이터 사용)
        timestamp=row['청소시기'],

        # 해안명
        coast_name=row['해안명'],

        # 해안 길이
        coast_length=row['해안길이(m)'],

        # 수거 마대 개수
        litter_bags_count=row['수거 마대 개수(개)'],

        # 수거량 환산 (엑셀 데이터 사용, 또는 자동 계산)
        calculated_litter_amount=row['수거량 환산(L, 마대 개수 * 50L)'],

        # 위도 및 경도
        latitude=row['위도'],
        longitude=row['경도'],

        # 주요 쓰레기 종류
        main_litter_type=row['주요쓰레기종류'],

        # 사진 필드 (엑셀에 없으므로 null로 설정)
        collection_photo=None,
        completion_photo_landscape=None,
        completion_photo_collection_site=None
    )

    # 데이터 저장
    cleanup.save()

print("Data imported successfully!")