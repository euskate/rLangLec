# 웹 스크래핑 예제
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹 페이지 요청
url = "http://www.competitorwebsite.com/products"  # 경쟁사 웹사이트 URL
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 예를 들어, 제품 목록과 가격을 추출한다고 가정
products = []
for product in soup.find_all('div', class_='product'):
    name = product.find('h2').text
    price = product.find('span', class_='price').text
    products.append({'name': name, 'price': price})

# 데이터프레임으로 변환
df_products = pd.DataFrame(products)
print(df_products.head())


# 데이터 전처리 : 수집한 데이터를 정제하여 분석 가능한 형태로 변환합니다.
# 가격을 숫자로 변환 (예: $10.99 -> 10.99)
df_products['price'] = df_products['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# 데이터 확인
print(df_products.describe())


# 데이터 분석 : 경쟁사의 제품 및 가격 데이터를 분석하여 인사이트를 도출합니다.
# 가격 분포 분석
import matplotlib.pyplot as plt
import seaborn as sns

# 가격 분포 시각화
plt.figure(figsize=(10, 6))
sns.histplot(df_products['price'], bins=30, kde=True, color='skyblue')
plt.title('Price Distribution of Competitor Products')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()


# 경쟁사 제품 가격 비교 : 경쟁사의 제품 가격을 다른 경쟁사와 비교하기 위해 가상의 데이터프레임을 사용합니다.
# 가상의 경쟁사 데이터
df_products_competitor = pd.DataFrame({
    'name': ['Product A', 'Product B', 'Product C'],
    'price': [15.99, 25.50, 12.75]
})

# 가격 비교 시각화
plt.figure(figsize=(10, 6))
df_products.plot(kind='bar', x='name', y='price', color='blue', label='Competitor A', alpha=0.6)
df_products_competitor.plot(kind='bar', x='name', y='price', color='red', label='Competitor B', alpha=0.6)
plt.title('Price Comparison between Competitors')
plt.xlabel('Product')
plt.ylabel('Price')
plt.legend()
plt.show()


# 인사이트 도출
# 가격 분포의 중심 경향 (평균, 중앙값)
mean_price = df_products['price'].mean()
median_price = df_products['price'].median()

print(f"Average Price: ${mean_price:.2f}")
print(f"Median Price: ${median_price:.2f}")

# 제품 가격의 변동성 분석
price_std = df_products['price'].std()
print(f"Price Standard Deviation: ${price_std:.2f}")


# 경쟁사의 전략 분석 : 분석 결과를 바탕으로 경쟁사의 가격 정책, 제품 라인업 등을 이해하고, 자신의 전략을 조정합니다.
# 예를 들어, 가격이 평균 이상인 제품 비율 계산
above_average = df_products[df_products['price'] > mean_price]
percentage_above_average = len(above_average) / len(df_products) * 100

print(f"Percentage of Products Above Average Price: {percentage_above_average:.2f}%")

