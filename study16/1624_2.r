install.packages("xgboost")
library(xgboost)

# 데이터 준비
data(iris)
iris_matrix <- as.matrix(iris[, -5])
labels <- as.numeric(iris$Species) - 1

# XGBoost 모델 학습
dtrain <- xgb.DMatrix(data = iris_matrix, label = labels)
params <- list(objective = "multi:softmax", num_class = 3)
model <- xgb.train(params, dtrain, nrounds = 10)

# 예측
preds <- predict(model, iris_matrix)
