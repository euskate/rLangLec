install.packages("data.table")
library(data.table)

# 데이터 생성
dt <- data.table(id = 1:1e6, value = rnorm(1e6))

# 데이터 처리
dt_summary <- dt[, .(mean_value = mean(value)), by = id]
print(dt_summary)
