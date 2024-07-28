# 패키지 설치 및 로드
install.packages("tree")
library(tree)

# 데이터 생성
set.seed(123)
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  y = factor(sample(c("A", "B"), 100, replace = TRUE))
)

# 의사결정트리 모델 생성 (분류)
model <- tree(y ~ x1 + x2, data = data)

# 모델 요약
summary(model)

# 모델 시각화
plot(model)
text(model)

# 예측
predictions <- predict(model, newdata = data, type = "class")
