# tidyr 패키지 로드
library(tidyr)

# 데이터 프레임 생성
data_long <- data.frame(
  Name = c("Alice", "Bob"),
  Year1 = c(85, 90),
  Year2 = c(88, 92)
)

# 데이터를 긴 형식으로 변환
data_wide <- pivot_longer(data_long, cols = starts_with("Year"), names_to = "Year", values_to = "Score")

# 변환된 데이터 출력
print(data_wide)
