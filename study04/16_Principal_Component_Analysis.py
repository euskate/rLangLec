import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. 데이터 생성
# 군집화에 적합한 데이터셋 생성
n_samples = 300
n_features = 5  # 고차원 데이터
n_clusters = 4
random_state = 42

X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=0.60, random_state=random_state)

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. PCA 모델 훈련
# PCA 객체 생성 (주성분 수 설정, 기본값은 None으로 모든 주성분을 유지함)
n_components = 2  # 2차원으로 축소
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

# 주성분 설명 비율
explained_variance_ratio = pca.explained_variance_ratio_
print(f"주성분 설명 비율: {explained_variance_ratio}")
print(f"누적 설명 비율: {np.cumsum(explained_variance_ratio)}")

# 3. 결과 시각화
plt.figure(figsize=(10, 7))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', s=50, cmap='viridis', label='데이터 포인트')
plt.title('PCA 결과 (2차원)')
plt.xlabel('주성분 1')
plt.ylabel('주성분 2')
plt.legend()
plt.grid(True)
plt.show()
