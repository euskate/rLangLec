df <- data.frame(id = 1:10, value = rnorm(10))

# 데이터 저장
write.csv(df, "data.csv", row.names = FALSE)

# 데이터 읽기
df_loaded <- read.csv("data.csv")
print(df_loaded)
