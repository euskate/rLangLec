import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. 데이터 생성
# 군집화에 적합한 데이터셋 생성
n_samples = 300
n_features = 2
n_clusters = 4
random_state = 42

X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=0.60, random_state=random_state)

# 2. 모델 훈련
# K-평균 군집화 모델 생성 (군집 수 K 설정)
kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
kmeans.fit(X)

# 예측된 군집 할당
y_kmeans = kmeans.predict(X)

# 3. 모델 평가 및 시각화
# 군집 중심
centers = kmeans.cluster_centers_

# 실루엣 점수 계산
silhouette_avg = silhouette_score(X, y_kmeans)
print(f"실루엣 점수: {silhouette_avg:.2f}")

# 결과 시각화
plt.figure(figsize=(10, 6))

# 원본 데이터 포인트 시각화
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis', label='데이터 포인트')

# 군집 중심 시각화
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='군집 중심')

plt.title('K-평균 군집화 결과')
plt.xlabel('특성 1')
plt.ylabel('특성 2')
plt.legend()
plt.grid(True)
plt.show()
