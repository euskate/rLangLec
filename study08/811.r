# 데이터 생성
set.seed(123)
data <- data.frame(
  x = rnorm(100),
  y = 2 * rnorm(100) + 3
)

# 선형 회귀 모델 생성
model <- lm(y ~ x, data = data)

# 모델 요약
summary(model)

# 예측
predictions <- predict(model, newdata = data.frame(x = c(-1, 0, 1)))
