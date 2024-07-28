install.packages("DBI")
install.packages("RSQLite")
library(DBI)
library(RSQLite)

# 데이터베이스 연결
con <- dbConnect(RSQLite::SQLite(), "my_database.sqlite")

# 데이터 프레임 생성
df <- data.frame(id = 1:10, value = rnorm(10))

# 데이터 저장
dbWriteTable(con, "my_table", df)

# 데이터 읽기
data <- dbReadTable(con, "my_table")
print(data)

# 연결 종료
dbDisconnect(con)
