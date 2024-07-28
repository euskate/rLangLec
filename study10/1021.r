# 패키지 설치 및 로드
install.packages("rpart")
library(rpart)

# 데이터 생성
set.seed(123)
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  y = factor(sample(c("A", "B"), 100, replace = TRUE))
)

# 의사결정트리 모델 생성 (분류)
model <- rpart(y ~ x1 + x2, data = data, method = "class")

# 모델 요약
print(model)

# 모델 시각화
library(rpart.plot)
rpart.plot(model)

# 예측
predictions <- predict(model, newdata = data, type = "class")
