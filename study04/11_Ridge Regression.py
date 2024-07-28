import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 로드 및 준비
# Boston 주택 데이터셋 로드
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.Series(boston.target, name='PRICE')

# 데이터셋을 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 데이터 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. 모델 훈련
# 릿지 회귀 모델 생성 (알파 값은 정규화 강도를 조절)
alpha = 1.0
ridge_model = Ridge(alpha=alpha)
ridge_model.fit(X_train, y_train)

# 3. 모델 평가
# 예측
y_pred = ridge_model.predict(X_test)

# 평균 제곱 오차 (MSE) 및 결정 계수 (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"평균 제곱 오차 (MSE): {mse:.2f}")
print(f"결정 계수 (R^2): {r2:.2f}")

# 회귀 계수 시각화
coefficients = ridge_model.coef_
features = X.columns

plt.figure(figsize=(10, 6))
plt.barh(features, coefficients)
plt.xlabel('회귀 계수')
plt.ylabel('특성')
plt.title('릿지 회귀 회귀 계수')
plt.show()

# 회귀 계수의 중요도 시각화
plt.figure(figsize=(10, 6))
plt.scatter(features, coefficients, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('특성')
plt.ylabel('회귀 계수')
plt.title('릿지 회귀 계수 중요도')
plt.show()
