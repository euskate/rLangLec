# 데이터 정제
# 결측값 처리 : 결측값(missing values)은 데이터를 분석하기 전에 반드시 처리해야 합니다. 대표적인 방법으로는 삭제, 평균값 또는 중앙값 대체 등이 있습니다.
import pandas as pd
import numpy as np

# 데이터 로드
data = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 'cat', 'dog', 'dog', 'cat'],
    'C': [10, 20, 30, 40, 50]
})

print("원본 데이터:")
print(data)

# 결측값 확인
print("\n결측값 확인:")
print(data.isna().sum())

# 결측값 처리
# 1. 결측값 삭제
data_cleaned = data.dropna()

# 2. 결측값 평균값으로 대체 (수치형 데이터에 대해)
data['A'].fillna(data['A'].mean(), inplace=True)

# 3. 결측값 최빈값으로 대체 (범주형 데이터에 대해)
data['B'].fillna(data['B'].mode()[0], inplace=True)

print("\n결측값 처리 후 데이터:")
print(data)


# 중복값 처리 : 중복된 데이터는 분석의 정확성을 해칠 수 있으므로 제거해야 합니다.
# 데이터 로드
data = pd.DataFrame({
    'A': [1, 2, 2, 4, 5],
    'B': ['cat', 'cat', 'dog', 'dog', 'cat'],
    'C': [10, 20, 20, 40, 50]
})

print("원본 데이터:")
print(data)

# 중복값 확인
print("\n중복값 확인:")
print(data.duplicated().sum())

# 중복값 제거
data_unique = data.drop_duplicates()

print("\n중복값 제거 후 데이터:")
print(data_unique)


# 이상값 처리 : 이상값(outliers)은 데이터 분석에서 영향을 미칠 수 있으므로 이를 식별하고 처리해야 합니다.
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 100],  # 이상값 포함
    'B': [10, 20, 30, 40, 50, 60]
})

print("원본 데이터:")
print(data)

# 이상값 시각화
plt.figure(figsize=(10, 5))
sns.boxplot(x=data['A'])
plt.title('Boxplot of A')
plt.show()

# IQR을 사용한 이상값 처리
Q1 = data['A'].quantile(0.25)
Q3 = data['A'].quantile(0.75)
IQR = Q3 - Q1

# 이상값 경계 설정
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 이상값 제거
data_filtered = data[(data['A'] >= lower_bound) & (data['A'] <= upper_bound)]

print("\n이상값 처리 후 데이터:")
print(data_filtered)


# 데이터 변환
# 정규화 : 정규화는 데이터의 스케일을 조정하여 동일한 범위로 변환하는 과정입니다.
from sklearn.preprocessing import MinMaxScaler

# 데이터 로드
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

print("원본 데이터:")
print(data)

# 정규화
scaler = MinMaxScaler()
data_normalized = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

print("\n정규화 후 데이터:")
print(data_normalized)


# 표준화 : 표준화는 데이터를 평균이 0, 표준편차가 1이 되도록 변환하는 과정입니다.
from sklearn.preprocessing import StandardScaler

# 데이터 로드
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

print("원본 데이터:")
print(data)

# 표준화
scaler = StandardScaler()
data_standardized = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

print("\n표준화 후 데이터:")
print(data_standardized)


# 범주형 데이터 인코딩 : 범주형 데이터는 머신러닝 모델이 이해할 수 있는 숫자형 데이터로 변환해야 합니다. 이를 위해 원-핫 인코딩을 사용할 수 있습니다.
# 데이터 로드
data = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C', 'B']
})

print("원본 데이터:")
print(data)

# 원-핫 인코딩
data_encoded = pd.get_dummies(data, columns=['Category'])

print("\n인코딩 후 데이터:")
print(data_encoded)


# 데이터 통합
# 데이터 조인 : 조인은 두 데이터프레임을 공통된 열을 기준으로 결합하는 과정입니다.
# 데이터 생성
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Value1': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Value2': ['X', 'Y', 'Z']
})

print("df1:")
print(df1)
print("\ndf2:")
print(df2)

# 데이터 조인 (내부 조인)
df_merged = pd.merge(df1, df2, on='ID', how='inner')

print("\n조인 결과:")
print(df_merged)


# 데이터 매핑 : 매핑은 한 데이터프레임의 값에 다른 데이터프레임의 값을 매핑하는 과정입니다.
# 데이터 생성
df_main = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Category': ['A', 'B', 'C', 'D']
})

df_mapping = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Description': ['Apple', 'Banana', 'Cherry', 'Date']
})

print("메인 데이터:")
print(df_main)
print("\n매핑 데이터:")
print(df_mapping)

# 데이터 매핑
df_main = df_main.merge(df_mapping, on='Category', how='left')

print("\n매핑 결과:")
print(df_main)