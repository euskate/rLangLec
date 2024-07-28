import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error

# 1. 시계열 데이터 준비
np.random.seed(0)

dates = pd.date_range(start='2020-01-01', periods=100, freq='D')
data = np.sin(np.linspace(0, 10, 100)) + np.random.normal(scale=0.5, size=100)
df = pd.DataFrame({'Date': dates, 'Value': data})
df.set_index('Date', inplace=True)

# 데이터 시각화
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Original Data')
plt.title('Original Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# 2. 시계열 분해
result = seasonal_decompose(df['Value'], model='additive')

plt.figure(figsize=(14, 10))

plt.subplot(4, 1, 1)
plt.plot(result.observed, label='Observed')
plt.legend(loc='upper left')

plt.subplot(4, 1, 2)
plt.plot(result.trend, label='Trend')
plt.legend(loc='upper left')

plt.subplot(4, 1, 3)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='upper left')

plt.subplot(4, 1, 4)
plt.plot(result.resid, label='Residual')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

# 3. ARIMA 모델 구축
plot_acf(df['Value'])
plt.title('ACF Plot')
plt.show()

plot_pacf(df['Value'])
plt.title('PACF Plot')
plt.show()

train_size = int(len(df) * 0.8)
train, test = df['Value'][:train_size], df['Value'][train_size:]

model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

forecast = model_fit.forecast(steps=len(test))
forecast_index = df.index[train_size:]

mse = mean_squared_error(test, forecast)
print(f"Mean Squared Error: {mse}")

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Value'], label='Original Data')
plt.plot(forecast_index, forecast, color='red', label='Forecast')
plt.title('ARIMA Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()
