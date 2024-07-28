# 패키지 설치 및 로드
install.packages("e1071")
library(e1071)

# 데이터 생성
set.seed(123)
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  y = factor(sample(c("Yes", "No"), 100, replace = TRUE))
)

# SVM 모델 생성
model <- svm(y ~ x1 + x2, data = data)

# 모델 요약
summary(model)

# 예측
predictions <- predict(model, newdata = data)
