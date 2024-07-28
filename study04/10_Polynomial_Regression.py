import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 생성
# 예제 데이터셋 생성: 1D 회귀 문제
X, y = make_regression(n_samples=100, n_features=1, noise=20, random_state=42)

# 2. 데이터 전처리
# 데이터셋을 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 데이터 스케일링 (선택 사항)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. 모델 훈련
# 다항식 특성 변환 (2차 다항식)
poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

# 다항 회귀 모델 생성
model = LinearRegression()
model.fit(X_poly_train, y_train)

# 4. 모델 평가 및 시각화
# 예측
y_pred = model.predict(X_poly_test)

# 평균 제곱 오차 (MSE) 및 결정 계수 (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"평균 제곱 오차 (MSE): {mse:.2f}")
print(f"결정 계수 (R^2): {r2:.2f}")

# 결과 시각화
# 훈련 데이터 및 테스트 데이터에 대한 예측 결과 시각화
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='실제 값')
plt.scatter(X_test, y_pred, color='red', label='예측 값')
plt.title('다항 회귀 결과')
plt.xlabel('특성')
plt.ylabel('타겟 값')
plt.legend()
plt.show()

# 시각화: 다항 회귀 결정 경계
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = model.predict(X_range_poly)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='실제 값')
plt.plot(X_range, y_range_pred, color='red', label='다항 회귀 예측')
plt.title('다항 회귀 결정 경계')
plt.xlabel('특성')
plt.ylabel('타겟 값')
plt.legend()
plt.show()
