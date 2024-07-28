import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns

# 1. 데이터 로드 및 준비
# 예제 데이터셋으로 `Iris` 데이터셋을 사용합니다.
from sklearn.datasets import load_iris

# Iris 데이터셋 로드
data = load_iris()
X = data.data
y = data.target

# 이진 분류 문제로 변환하기 위해, 클래스 0과 1만 사용
X = X[y != 2]
y = y[y != 2]

# 데이터셋을 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 데이터 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. 모델 훈련
# KNN 모델 생성 (K=3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 3. 모델 평가
# 예측
y_pred = model.predict(X_test)

# 정확도
accuracy = accuracy_score(y_test, y_pred)
print(f"정확도: {accuracy:.2f}")

# 혼동 행렬
cm = confusion_matrix(y_test, y_pred)
print("\n혼동 행렬:")
print(cm)

# 혼동 행렬 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
plt.xlabel('예측된 클래스')
plt.ylabel('실제 클래스')
plt.title('혼동 행렬')
plt.show()

# 분류 리포트
report = classification_report(y_test, y_pred)
print("\n분류 리포트:")
print(report)

# 4. 결과 시각화
# 결정 경계 시각화 (2D 특성만 사용)
def plot_decision_boundary(X, y, model):
    h = .02  # 간격의 크기
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', marker='o', cmap=plt.cm.Paired)
    plt.xlabel('특성 1')
    plt.ylabel('특성 2')
    plt.title('결정 경계')
    plt.show()

# 데이터가 2D로 변환된 상태에서 결정 경계 시각화
X_train_2d = X_train[:, :2]  # 첫 2개 특성만 사용
X_test_2d = X_test[:, :2]
model_2d = KNeighborsClassifier(n_neighbors=3)
model_2d.fit(X_train_2d, y_train)
plot_decision_boundary(X_test_2d, y_test, model_2d)
