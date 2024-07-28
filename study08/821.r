# 데이터 생성
set.seed(123)
data <- data.frame(
  x = rnorm(100),
  y = factor(sample(c("Yes", "No"), 100, replace = TRUE))
)

# 로지스틱 회귀 모델 생성
model <- glm(y ~ x, data = data, family = binomial)

# 모델 요약
summary(model)

# 예측 확률
predictions <- predict(model, type = "response")
