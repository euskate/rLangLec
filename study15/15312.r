install.packages("dplyr")
install.packages("dbplyr")
library(dplyr)
library(dbplyr)

# 데이터 전처리와 데이터베이스 연결
# 데이터 생성
df <- tibble(id = 1:1000, value = rnorm(1000))

# 데이터 전처리
df_processed <- df %>%
  filter(value > 0) %>%
  mutate(squared_value = value^2) %>%
  group_by(id) %>%
  summarize(mean_value = mean(squared_value))

# 데이터베이스 연결 예제
# DBI와 RSQLite 패키지 필요
# install.packages("DBI")
# install.packages("RSQLite")
library(DBI)
library(RSQLite)

# 데이터베이스 연결
con <- dbConnect(RSQLite::SQLite(), ":memory:")
dbWriteTable(con, "large_data", df)
query <- tbl(con, "large_data") %>%
  filter(value > 0) %>%
  summarize(count = n())
query_result <- collect(query)
print(query_result)
