import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

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
# DBSCAN 군집화 모델 생성
eps = 0.5  # 이웃으로 간주할 거리
min_samples = 5  # 군집의 최소 샘플 수
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
y_dbscan = dbscan.fit_predict(X_scaled)

# 3. 모델 평가 및 시각화
# 군집의 고유한 레이블 (노이즈는 -1로 표시됨)
unique_labels = np.unique(y_dbscan)
n_clusters_ = len(unique_labels) - (1 if -1 in unique_labels else 0)

# 실루엣 점수 계산 (노이즈가 포함되어 있는 경우, 노이즈를 제외한 데이터만 사용)
if n_clusters_ > 1:
    silhouette_avg = silhouette_score(X_scaled, y_dbscan)
    print(f"실루엣 점수: {silhouette_avg:.2f}")
else:
    print("군집이 1개 이하로 평가되었습니다. 실루엣 점수를 계산할 수 없습니다.")

# 결과 시각화
plt.figure(figsize=(10, 7))

# 군집화 결과 시각화
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_dbscan, s=50, cmap='viridis', label='데이터 포인트')

# 노이즈 포인트를 다른 색으로 표시
plt.scatter(X_scaled[y_dbscan == -1, 0], X_scaled[y_dbscan == -1, 1], c='red', s=50, marker='x', label='노이즈')

plt.title('DBSCAN 군집화 결과')
plt.xlabel('특성 1')
plt.ylabel('특성 2')
plt.legend()
plt.grid(True)
plt.show()
