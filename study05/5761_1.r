# dplyr 패키지 로드
library(dplyr)

# 데이터 프레임 생성
data <- data.frame(Name=c("Alice", "Bob", "Charlie"), Age=c(25, 30, 35))

# 필터링
filtered_data <- filter(data, Age > 30)

# 필터링된 데이터 출력
print(filtered_data)
