import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler

# 1. 데이터 생성
# 군집화에 적합한 데이터셋 생성
n_samples = 300
n_features = 2
n_clusters = 4
random_state = 42

X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=0.60, random_state=random_state)

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. 모델 훈련
# 계층적 군집화 모델 생성
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters)
y_agg = agg_clustering.fit_predict(X_scaled)

# 3. 모델 평가 및 시각화
# 덴드로그램 시각화
plt.figure(figsize=(10, 7))
linked = linkage(X_scaled, 'ward')
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('덴드로그램')
plt.xlabel('데이터 포인트')
plt.ylabel('거리')
plt.show()

# 결과 시각화
plt.figure(figsize=(10, 7))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_agg, s=50, cmap='viridis', label='데이터 포인트')
plt.title('계층적 군집화 결과')
plt.xlabel('특성 1')
plt.ylabel('특성 2')
plt.legend()
plt.grid(True)
plt.show()
