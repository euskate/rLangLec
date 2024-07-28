import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

# 1. 데이터 생성
# 군집화에 적합한 데이터셋 생성
n_samples = 300
n_features = 5  # 고차원 데이터
n_clusters = 4
random_state = 42

X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=0.60, random_state=random_state)

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. t-SNE 모델 훈련
# t-SNE 객체 생성 (주성분 수를 2로 설정하여 2차원으로 축소)
tsne = TSNE(n_components=2, random_state=random_state)
X_tsne = tsne.fit_transform(X_scaled)

# 3. 결과 시각화
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, s=50, cmap='viridis', label='데이터 포인트')
plt.colorbar(scatter, label='클러스터')
plt.title('t-SNE 결과 (2차원)')
plt.xlabel('t-SNE 차원 1')
plt.ylabel('t-SNE 차원 2')
plt.legend()
plt.grid(True)
plt.show()
