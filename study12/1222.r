install.packages("kernlab")
library(kernlab)

# Iris 데이터셋 로드
data(iris)

# SVM 모델 학습 (Species를 예측)
model <- ksvm(Species ~ ., data = iris, kernel = "rbf")

# 모델 요약
summary(model)

# 예측
predictions <- predict(model, iris)

# 혼동 행렬
table(predictions, iris$Species)
