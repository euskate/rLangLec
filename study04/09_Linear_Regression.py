import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

# 1. 데이터 로드 및 준비
# Boston 주택 데이터셋 로드
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.Series(boston.target, name='PRICE')

# 데이터셋을 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. 모델 훈련
model = LinearRegression()
model.fit(X_train, y_train)

# 3. 모델 평가
# 예측
y_pred = model.predict(X_test)

# 평균 제곱 오차 (MSE) 및 결정 계수 (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"평균 제곱 오차 (MSE): {mse:.2f}")
print(f"결정 계수 (R^2): {r2:.2f}")

# 회귀 계수 시각화
coefficients = model.coef_
features = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=features, y=coefficients)
plt.xticks(rotation=90)
plt.xlabel('특성')
plt.ylabel('계수')
plt.title('회귀 계수')
plt.show()

# 결과 시각화: 예측 값과 실제 값의 산점도
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.xlabel('실제 값')
plt.ylabel('예측 값')
plt.title('실제 값 vs 예측 값')
plt.show()
