library(DBI)
library(RSQLite)

# 데이터베이스 연결
con <- dbConnect(RSQLite::SQLite(), "secure_database.sqlite")

# 쿼리 실행
data <- dbGetQuery(con, "SELECT * FROM confidential_data")

# 연결 종료
dbDisconnect(con)
