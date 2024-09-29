import os
import django
import pandas as pd

# Django 설정 파일 경로 지정 (settings.py가 위치한 경로)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ocean.settings')  # your_project_name을 실제 프로젝트 이름으로 수정
django.setup()

# Django 모델 가져오기
from investigation.models import Investigation

# 엑셀 파일 경로 수정
excel_file_path = '/Users/ieunjin/Downloads/invest.xlsx'  # 엑셀 파일 경로 설정

# 엑셀 파일 읽기
df = pd.read_excel(excel_file_path)
df['조사시기'] = pd.to_datetime(df['조사시기'], format='%Y/%m/%d %H:%M:%S')

# 각 행을 Django 모델로 변환하여 저장
for index, row in df.iterrows():
    investigation = Investigation(
        # 조사자 성명
        investigator_name=row['조사자 성명'],

        # 조사 일련번호 (엑셀 데이터 사용 또는 자동 생성)
        investigation_serial_number=row['조사 일련번호'],

        # 조사 시기 (엑셀 데이터 사용)
        timestamp=row['조사시기'],

        # 해안명
        coast_name=row['해안명'],

        # 해안 길이
        coast_length=row['해안길이(m)'],

        # 수거 예측량
        estimated_litter_amount=row['예측량(L)'],

        # 위도 및 경도
        latitude=row['위도'],
        longitude=row['경도'],

        # 주요 쓰레기 종류
        main_litter_type=row['주요쓰레기종류'],

        # 사진 필드 (엑셀에 없으므로 null로 설정)
        photo=None
    )

    # 조사 일련번호 자동 생성 (엑셀에서 제공되지 않으면 자동 생성)
    if pd.isnull(investigation.investigation_serial_number):
        investigation.investigation_serial_number = investigation.generate_serial_number()

    # 데이터 저장
    investigation.save()

print("Investigation data imported successfully!")