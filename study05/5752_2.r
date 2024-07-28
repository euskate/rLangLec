# writexl 패키지 설치
install.packages("writexl")

# writexl 패키지 로드
library(writexl)

# 데이터 프레임 생성
data <- data.frame(Name=c("Alice", "Bob"), Age=c(25, 30))

# Excel 파일 쓰기
write_xlsx(data, "output.xlsx")
