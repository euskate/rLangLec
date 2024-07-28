install.packages("caret")
library(caret)

# Iris 데이터셋 로드
data(iris)

# 데이터 분할
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = .8, list = FALSE)
trainData <- iris[trainIndex,]
testData <- iris[-trainIndex,]

# SVM 모델 학습
model <- train(Species ~ ., data = trainData, method = "svmLinear")

# 모델 요약
print(model)

# 예측
predictions <- predict(model, testData)

# 혼동 행렬
confusionMatrix(predictions, testData$Species)
