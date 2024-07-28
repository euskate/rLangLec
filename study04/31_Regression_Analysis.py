import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 준비
np.random.seed(0)

# 예제 데이터 생성 (선형 관계)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 2 * X.flatten() + 1 + np.random.normal(scale=1, size=X.shape[0])

# 데이터 프레임으로 변환
df = pd.DataFrame({'X': X.flatten(), 'y': y})

# 2. 선형 회귀 (Linear Regression)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 선형 회귀 모델 생성 및 학습
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# 예측
y_pred_train = linear_reg.predict(X_train)
y_pred_test = linear_reg.predict(X_test)

# 평가
print("Linear Regression")
print("Training Mean Squared Error:", mean_squared_error(y_train, y_pred_train))
print("Testing Mean Squared Error:", mean_squared_error(y_test, y_pred_test))
print("Training R^2 Score:", r2_score(y_train, y_pred_train))
print("Testing R^2 Score:", r2_score(y_test, y_pred_test))

# 시각화
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, linear_reg.predict(X), color='red', label='Linear Fit')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# 3. 다항 회귀 (Polynomial Regression)
poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(X)

# 데이터 분리
X_train_poly, X_test_poly, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=0)

# 다항 회귀 모델 생성 및 학습
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)

# 예측
y_pred_poly = poly_reg.predict(X_test_poly)

# 평가
print("\nPolynomial Regression (degree=3)")
print("Testing Mean Squared Error:", mean_squared_error(y_test, y_pred_poly))
print("Testing R^2 Score:", r2_score(y_test, y_pred_poly))

# 시각화
plt.subplot(1, 2, 2)
X_grid = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_grid_poly = poly_features.transform(X_grid)
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_grid, poly_reg.predict(X_grid_poly), color='green', label='Polynomial Fit (degree=3)')
plt.title('Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
