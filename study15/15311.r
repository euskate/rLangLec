install.packages("data.table")
library(data.table)

# 큰 데이터셋의 처리
# 대규모 데이터 생성
set.seed(123)
large_data <- data.table(id = 1:1e6, value = rnorm(1e6))

# 데이터 요약
summary(large_data)

# 필터링 및 집계
filtered_data <- large_data[value > 0]
summary(filtered_data)
