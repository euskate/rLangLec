import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 준비
np.random.seed(0)

data = {
    'X1': np.random.normal(loc=0, scale=1, size=1000),  # 정규분포 데이터
    'X2': np.random.normal(loc=5, scale=2, size=1000),  # 정규분포 데이터
    'Category': np.random.choice(['A', 'B', 'C'], size=1000)  # 카테고리 변수
}

df = pd.DataFrame(data)

# 산점도 (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='X1', y='X2', data=df, hue='Category', palette='viridis')
plt.title('Scatter Plot of X1 vs X2')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend(title='Category')
plt.show()

# 히스토그램 (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['X1'], bins=30, kde=True, color='blue', alpha=0.7)
plt.title('Histogram of X1')
plt.xlabel('X1')
plt.ylabel('Frequency')
plt.show()

# 상자 그림 (Box Plot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='X2', data=df, palette='Set2')
plt.title('Box Plot of X2 by Category')
plt.xlabel('Category')
plt.ylabel('X2')
plt.show()
