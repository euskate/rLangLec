# 패키지 설치 및 로드
install.packages("C50")
library(C50)

# 데이터 생성
set.seed(123)
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  y = factor(sample(c("A", "B"), 100, replace = TRUE))
)

# C5.0 모델 생성
model <- C5.0(x = data[, c("x1", "x2")], y = data$y)

# 모델 요약
summary(model)

# 예측
predictions <- predict(model, newdata = data)
