# readxl 패키지 설치
install.packages("readxl")

# readxl 패키지 로드
library(readxl)

# Excel 파일 읽기
data <- read_excel("data.xlsx")

# 데이터 출력
print(data)
