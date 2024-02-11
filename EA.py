import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
import matplotlib.font_manager as fm

# 폰트 경로 지정
font_path = r'C:\Users\oh\Desktop\D2CodingAll\D2Coding-Ver1.3.2-20180524-all.ttc'  # 한글 폰트 파일 경로에 맞게 수정

# 폰트 이름 가져오기
font_name = fm.FontProperties(fname=font_path).get_name()

# 폰트 설정
plt.rc('font', family=font_name)


# 데이터 파일 불러오기
customer_data = pd.read_csv(r"C:\Users\oh\Desktop\e-commerce\e-commerce\Customer_info.csv")
discount_data = pd.read_csv(r"C:\Users\oh\Desktop\e-commerce\e-commerce\Discount_info.csv")
marketing_data = pd.read_csv(r"C:\Users\oh\Desktop\e-commerce\e-commerce\Marketing_info.csv")
tax_data = pd.read_csv(r"C:\Users\oh\Desktop\e-commerce\e-commerce\Tax_info.csv")
onlinesales_data = pd.read_csv(r"C:\Users\oh\Desktop\e-commerce\e-commerce\Onlinesales_info.csv")

# 데이터 전처리
## 결측치 확인하기
customer_data.isnull().sum()
discount_data.isnull().sum()
marketing_data.isnull().sum()
tax_data.isnull().sum()
onlinesales_data.isnull().sum()
# 결측치는 없는 걸로 확인 된다

# 'Transaction_Date' 컬럼을 날짜 타입으로 변환하고 월별로 집계
# 'Month' 컬럼으로 거래량 계산
counts_by_month = onlinesales_data.assign(Month=pd.to_datetime(onlinesales_data['거래날짜']).dt.to_period('M'))['Month'].value_counts().sort_index()

# 시간에 따른 거래량 선 그래프 그리기
plt.figure(figsize=(15, 6))
sns.lineplot(x=counts_by_month.index.astype(str), y=counts_by_month.values)
plt.title('시간에 따른 거래량')
plt.xlabel('월')
plt.ylabel('거래량')
plt.xticks(rotation=45)
plt.show()

gender_counts = customer_data['성별'].value_counts()

# 원그래프 그리기
plt.figure(figsize=(8, 8))  # 그래프 크기 설정
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)  # 원그래프 그리기
plt.title('성별 시각화')  # 그래프 제목 설정
plt.show()  # 그래프 보여주기


# customers_data에서 '고객지역' 열을 사용하여 지역별 거래량 계산
location_counts = customer_data['고객지역'].value_counts()

# 바 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
sns.barplot(x=location_counts.index, y=location_counts.values)  # seaborn을 사용한 바 그래프 그리기
plt.title('고객 지역 시각화')  # 그래프 제목 설정
plt.xlabel('고객지역')  # x축 레이블 설정
plt.xticks(rotation=45)  # x축 레이블 회전
plt.show()  # 그래프 보여주기

