install.packages("LiblineaR")
library(LiblineaR)

# Iris 데이터셋 로드
data(iris)

# 데이터 준비
x <- as.matrix(iris[, -5])
y <- as.factor(iris$Species)

# SVM 모델 학습 (선형 커널)
model <- LiblineaR(data = x, target = y, type = 0)

# 예측
predictions <- predict(model, x)$predictions

# 혼동 행렬
table(predictions, y)
