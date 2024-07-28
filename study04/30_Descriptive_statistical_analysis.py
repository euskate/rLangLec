import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 준비
np.random.seed(0)

data = {
    'X1': np.random.normal(loc=0, scale=1, size=1000),  # 정규분포 데이터
    'X2': np.random.normal(loc=5, scale=2, size=1000),  # 정규분포 데이터
    'X3': np.random.normal(loc=-3, scale=0.5, size=1000)  # 정규분포 데이터
}

df = pd.DataFrame(data)

# 2. 기술 통계량 계산
mean = df.mean()
median = df.median()
std_dev = df.std()

print("Mean:\n", mean)
print("\nMedian:\n", median)
print("\nStandard Deviation:\n", std_dev)

# 3. 상관 분석
correlation_matrix = df.corr()

print("\nCorrelation Matrix:\n", correlation_matrix)

# 4. 상관 행렬 시각화
plt.figure(figsize=(10, 7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
