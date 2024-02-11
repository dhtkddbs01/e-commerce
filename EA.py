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

# 세금에 따른 주문 수량 확인
