# 패키지 설치 및 로드
install.packages("randomForestSRC")
library(randomForestSRC)

# 데이터 생성
set.seed(123)
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  y = factor(sample(c("A", "B"), 100, replace = TRUE))
)

# 랜덤 포레스트 모델 생성 (분류)
model <- rfsrc(y ~ x1 + x2, data = data, ntree = 100)

# 모델 요약
print(model)

# 예측
predictions <- predict(model, newdata = data)$class

# 중요 변수 시각화
plot(model, main = "Variable Importance")
