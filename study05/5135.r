# readr 패키지 사용 예시
library(readr)
df_csv <- read_csv("data.csv")
write_csv(df_csv, "output.csv")

# data.table 패키지 사용 예시
library(data.table)
df_csv_fast <- fread("data.csv")
fwrite(df_csv_fast, "output_fast.csv")

# readxl 패키지 사용 예시
library(readxl)
df_excel <- read_excel("data.xlsx", sheet = 1)

# openxlsx 패키지 사용 예시
library(openxlsx)
df_excel_write <- data.frame(Name = c("John", "Jane"), Age = c(30, 25))
write.xlsx(df_excel_write, "output.xlsx", sheetName = "Sheet1")
