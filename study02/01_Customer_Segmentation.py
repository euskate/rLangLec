# 데이터 다운로드 및 로드
import pandas as pd

# 데이터 로드 (CSV 파일을 로드한다고 가정)
# 실제 파일 경로를 지정해야 합니다.
data = pd.read_csv('customer_data.csv')

# 데이터 확인
print(data.head())


# 데이터 전처리 : 데이터 전처리는 결측치 처리, 특성 선택, 데이터 정규화 등을 포함합니다.
# 결측치 처리 (평균값으로 대체 또는 삭제)
data = data.fillna(data.mean())

# 특성 선택 (클러스터링에 사용할 변수만 선택)
features = data[['age', 'income', 'spending_score']]  # 예시 특성

# 데이터 정규화 (표준화)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print(pd.DataFrame(scaled_features, columns=features.columns).head())


# K-평균 클러스터링 모델 생성 및 학습
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 클러스터 수 설정 (예: 5개 클러스터)
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(scaled_features)

# 클러스터 라벨 추출
data['cluster'] = kmeans.labels_

# 클러스터 중심 추출
centers = kmeans.cluster_centers_

# 클러스터 중심 시각화 (2차원 데이터의 경우)
plt.scatter(scaled_features[:, 0], scaled_features[:, 1], c=data['cluster'], cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')  # 클러스터 중심
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.show()


# 클러스터별 통계량 계산
# 클러스터별 통계량
cluster_summary = data.groupby('cluster').mean()
print(cluster_summary)

# 각 클러스터의 고객 수 확인
cluster_counts = data['cluster'].value_counts()
print(cluster_counts)


# 클러스터별 고객 프로파일 생성
# 클러스터별 고객 프로파일
for cluster in range(5):
    cluster_data = data[data['cluster'] == cluster]
    print(f"Cluster {cluster} Profile:")
    print(cluster_data[['age', 'income', 'spending_score']].describe())


# 클러스터별 시각화
import seaborn as sns

# 클러스터별 시각화 (예: 소득과 소비 점수)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='income', y='spending_score', hue='cluster', palette='viridis')
plt.title('Customer Segmentation')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.legend(title='Cluster')
plt.show()