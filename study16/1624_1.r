install.packages("caret")
library(caret)

# 데이터 준비
data(iris)
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = .8, list = FALSE)
trainData <- iris[trainIndex,]
testData <- iris[-trainIndex,]

# 모델 학습
model <- train(Species ~ ., data = trainData, method = "rf")

# 예측
predictions <- predict(model, testData)

# 혼동 행렬
confusionMatrix(predictions, testData$Species)
